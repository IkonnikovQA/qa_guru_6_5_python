from selene import browser, be, have, command
import os


def test_new_user_all_fields_all_valid():
    # Form creation steps
    browser.open('/automation-practice-form')
    browser.element('#firstName').should(be.blank).type('Stepan')
    browser.element('#lastName').should(be.blank).type('Ivanov')
    browser.element('#userEmail').should(be.blank).type('nonexisting@reallynonexisting.nono')
    browser.all('#genterWrapper .custom-control').element_by(have.exact_text('Male')).click()
    browser.element('#userNumber').should(be.blank).type('1234567890')
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__year-select [value="1991"]').click()
    browser.element('.react-datepicker__month-select [value="7"]').click()
    browser.element('.react-datepicker__day--008').click()
    # another option to set DoB
    browser.element('#dateOfBirthInput').perform(command.select_all).send_keys('08 Aug 1991').press_enter()
    browser.element('#subjectsInput').type('comp').press_enter()
    browser.all('#hobbiesWrapper .custom-control')[0].click()
    browser.element('#uploadPicture').send_keys(os.getcwd() + '/resources/test.jpeg')
    browser.element('#currentAddress').should(be.blank).type('Test str.')
    browser.element('#state').click()
    browser.element('#state #react-select-3-option-0').click()
    browser.element('#city').click()
    browser.element('#city #react-select-4-option-0').click()
    browser.element('#submit').click()

    # # Tests for data submitted
    browser.element('.modal-header').should(have.exact_text('Thanks for submitting the form'))
    browser.all('.modal-body tr td')[1].should(have.exact_text('Stepan Ivanov'))
    browser.all('.modal-body tr td')[3].should(have.exact_text('nonexisting@reallynonexisting.nono'))
    browser.all('.modal-body tr td')[5].should(have.exact_text('Male'))
    browser.all('.modal-body tr td')[7].should(have.exact_text('1234567890'))
    browser.all('.modal-body tr td')[9].should(have.exact_text('08 August,1991'))
    browser.all('.modal-body tr td')[11].should(have.exact_text('Computer Science'))
    browser.all('.modal-body tr td')[13].should(have.exact_text('Sports'))
    browser.all('.modal-body tr td')[15].should(have.exact_text('test.jpeg'))
    browser.all('.modal-body tr td')[17].should(have.exact_text('Test str.'))
    browser.all('.modal-body tr td')[19].should(have.text('NCR Delhi'))

    # Close modal: step and test result
    browser.element('#closeLargeModal').click()
    browser.element('.modal-dialog').should(be.absent)
    browser.element('#firstName').should(be.blank)