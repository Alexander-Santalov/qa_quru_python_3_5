import os
from selene import have
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


def test_registration(app):
    app.open("/automation-practice-form")
    app.element("#firstName").set_value("Alexander")
    app.element("#lastName").set_value("Santalov")
    app.element("#userEmail").set_value("asantalov@bolid.ru")
    app.element("#userNumber").set_value("8916777665")
    app.element("[for='gender-radio-1']").click()
    app.element("#dateOfBirthInput").click()
    ActionChains(app.driver).key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).perform()
    app.element("#dateOfBirthInput").send_keys("03 Aug 1986")
    ActionChains(app.driver).key_down(Keys.ESCAPE).perform()
    app.element("#subjectsInput").set_value("Chemistry").press_enter()
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
        'Alexander Santalov', 'asantalov@bolid.ru', 'Male', '8916777665', '03 August,1986', 'Chemistry',
        'Sports, Music', 'Toolsqa.jpg', 'Zelenograd', 'Haryana Panipat'))
    app.element("#closeLargeModal").click()
