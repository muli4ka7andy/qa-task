import os

from playwright.sync_api import Page
from ui_tests.locators.upload_page import UploadPageLocators as Locators

def test_file_upload(page: Page, upload_page_url):
    page.goto(upload_page_url)
    file_path = os.path.abspath("sample.txt")
    with open(file_path, "w") as f:
        f.write("Test file upload")

    page.set_input_files(Locators.FILE_INPUT, file_path)
    page.click(Locators.SUBMIT_BUTTON)

    assert page.text_content(Locators.SUCCESS_HEADER) == "File Uploaded!"
    assert "sample.txt" in page.text_content(Locators.UPLOADED_FILES_TEXT)

def test_upload_without_file_should_fail_with_200(page: Page, upload_page_url):

    page.goto(upload_page_url)

    with page.expect_navigation() as nav_info:
        page.click(Locators.SUBMIT_BUTTON)
    response = nav_info.value

    assert response.status == 200, f"Expected 200 OK, but got {response.status}"

def test_real_drag_drop_emulation(page: Page):
    page.set_content("""
        <html>
        <body>
            <div id="dropzone" style="width:200px; height:100px; border:2px dashed black;">
              Drop files here
            </div>
            <script>
                window.droppedFileName = null;
                const dropzone = document.getElementById('dropzone');
                dropzone.addEventListener('drop', (event) => {
                    event.preventDefault();
                    window.droppedFileName = event.dataTransfer.files[0].name;
                });
                dropzone.addEventListener('dragover', (event) => event.preventDefault());
            </script>
        </body>
        </html>
    """)

    file_path = os.path.abspath("dragdrop.txt")
    with open(file_path, "w") as f:
        f.write("Simulated drag-drop content")

    page.evaluate(
        """async () => {
            const file = new File(["Simulated drag-drop content"], "dragdrop.txt", { type: "text/plain" });
            const dataTransfer = new DataTransfer();
            dataTransfer.items.add(file);
            const dropzone = document.getElementById("dropzone");
            const event = new DragEvent("drop", {
                dataTransfer,
                bubbles: true,
                cancelable: true
            });
            dropzone.dispatchEvent(event);
        }"""
    )

    file_name = page.evaluate("() => window.droppedFileName")
    assert file_name == "dragdrop.txt"

def test_check_all_text_elements_in_english(page: Page, upload_page_url):
    page.goto(upload_page_url)

    expected_texts = {
        "h3": "File Uploader",
        "p": "Choose a file on your system and then click upload. Or, drag and drop a file into the area below.",
        "div[style='text-align: center;']": "Powered by Elemental Selenium",
    }

    for selector, expected_text in expected_texts.items():
        element = page.locator(selector)
        actual_text = element.inner_text().strip()

        assert actual_text == expected_text, (
            f"Text mismatch for '{selector}':\n"
            f"Expected: '{expected_text}'\n"
            f"Actual:   '{actual_text}'"
        )
