import os
from selene import have


def test_registration(app):
    app.open("/automation-practice-form")
    app.element("#firstName").set_value("Alexander")
    app.element("#lastName").set_value("Santalov")
    app.element("#userEmail").set_value("asantalov@bolid.ru")
    app.element("#userNumber").set_value("89167776655")
    app.element("[for='gender-radio-1']").click()
    app.element("#dateOfBirthInput").execute_script("element.value ='03 Aug 1986'")
    app.element("#subjectsInput").set_value("physical education")
    app.element("[for='hobbies-checkbox-1']").click()
    app.element("[for='hobbies-checkbox-3']").click()
    app.element("#uploadPicture").set_value(
        os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir, 'upload/Toolsqa.jpg')))
    app.element("#currentAddress").set_value("Zelenograd")
    app.element("#state").click().element("#react-select-3-option-2").click()
    app.element("#city").click().element("#react-select-4-option-1").click()
    app.element("#submit").execute_script("element.click()")
    app.all("tbody tr").should(have.size(10))
    app.all("tbody tr td:last-child").should(have.exact_texts(
        "Alexander Santalov", "asantalov@bolid.ru", "Male", "8916777665", "03 December,2022", "physical education",
        "Sports, Music", "Toolsqa.jpg", "Zelenograd", "Haryana Panipat"))
    app.element("#closeLargeModal").click()
