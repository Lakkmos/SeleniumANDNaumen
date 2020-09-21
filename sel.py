from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time,sys,mass
from PyQt5 import QtCore, QtGui, QtWidgets
global driver, array
array =[]


class massshoting (QtWidgets.QMainWindow, mass.Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
       # array = []
        self.buttonBox.clicked.connect(self.push)
        self.comboBox.activated[int].connect(self.changec)
        self.button.clicked.connect(self.take)

    def changec(self):
        if self.comboBox.currentText() == "Смена профиля (только из Default)":
            self.label_2.setText('Имя профиля')
            self.comboBox_1.setVisible(False)
            self.lineEdit_5.setVisible(False)
            self.label_6.setVisible(False)
            self.button.setVisible(False)
        elif self.comboBox.currentText() == "Назначение СВ":
            self.label_2.setText('ФИО СВ')
            self.comboBox_1.setVisible(False)
            self.lineEdit_5.setVisible(False)
            self.label_6.setVisible(False)
            self.button.setVisible(False)
        else:
            self.label_2.setText('Название скила')
            self.lineEdit_5.setVisible(True)
            self.label_6.setVisible(True)
            self.button.setVisible(True)

    def take(self):
        global skills
        skills={}
        self.comboBox_1.clear()
        self.start()
        driver.get("http://10.77.1.111:8080/form?uuid=corebo00000000000mtvuntc1j56fu48&activeComponent=Employee.ListsParent.ListsParent2.SkillList.addObjectSkillRelation")
        el = driver.find_element_by_id("htmlId")
        time.sleep(1)
        el.find_element_by_id("skill_box").click()
        elem = el.find_elements_by_tag_name('a')
        self.comboBox_1.setVisible(True)
        for e in elem:
            skills[str(e.text)] = e.get_attribute('rel')
            if str(e.text) != '':
                self.comboBox_1.addItem(str(e.text))
        driver.close()

    def push(self):
        global array
        if self.comboBox.currentText() == "Добавление навыков":
            array = []
            self.progressBar.setValue(0)
            self.start()
            self.reaper()
            i=1
            for u in array:
                self.add_skill(u)
                self.progressBar.setValue(i*(100//len(array)))
                i += 1
            self.progressBar.setValue(100)
        elif self.comboBox.currentText() == "Удаление навыков":
            array = []
            self.progressBar.setValue(0)
            self.start()
            self.reaper()
            i = 1
            for u in array:
                self.delete_skill(u)
                self.progressBar.setValue(i * (100 // len(array)))
                i += 1
            self.progressBar.setValue(100)
        elif self.comboBox.currentText() == "Смена профиля (только из Default)":
            array = []
            self.progressBar.setValue(0)
            self.start()
            self.reaper()
            i = 1
            for u in array:
                self.change_profile_d(u)
                self.progressBar.setValue(i * (100 // len(array)))
                i += 1
            self.progressBar.setValue(100)
        elif self.comboBox.currentText() == "Назначение СВ":
            array = []
            self.progressBar.setValue(0)
            self.start()
            self.tree()
            i = 1
            for u in array:
                self.add_sv(u)
                self.progressBar.setValue(i * (100 // len(array)))
                i += 1
            self.progressBar.setValue(100)

    def start(self):
        global driver
        driver = webdriver.Firefox(executable_path=r"geckodriver.exe")
        if self.checkBox.isChecked() == False:
            driver.minimize_window()
        driver.get("http://10.77.1.111:8080/")
        assert "VOX COM" in driver.title
        elem = driver.find_element_by_name("login")
        login = self.lineEdit_3.text()
        elem.send_keys(login)
        elem = driver.find_element_by_name("password")
        password = self.lineEdit_4.text()
        elem.send_keys(password)
        elem.send_keys(Keys.RETURN)
        time.sleep(2)

    def search_ou(self):
        driver.find_element_by_id("SystemSearch").click()
        elem = driver.find_element_by_id("searchString")
        elem.send_keys("Битые логины")
        elem = driver.find_element_by_id("searchTypeSelect_outer")
        elem.click()
        driver.find_element_by_xpath('//a[@rel="ou"]').click()
        time.sleep(1)
        driver.find_element_by_id("doSearch_outer").click()

    def search_employee(self):
        driver.find_element_by_id("SystemSearch").click()
        elem = driver.find_element_by_id("searchString")
        elem.send_keys("Абрамешин Кирилл")
        elem = driver.find_element_by_id("searchTypeSelect_outer")
        elem.click()
        driver.find_element_by_xpath('//a[@rel="employee"]').click()
        time.sleep(1)
        driver.find_element_by_id("doSearch_outer").click()

    def reaper(self):
        global array
        linki = []
        url = self.lineEdit_2.text()
        driver.get(url)
        links = driver.find_element_by_id("leftColumn")
        links = links.find_elements_by_tag_name("a")
        for link in links:
            linki.append(str(link.get_attribute("href")))
        for link in linki:
            driver.get(link)
            time.sleep(2)
            elem = driver.find_element_by_id("OU.ListsParent.EmployeesList")
            all_options = elem.find_elements_by_tag_name("a")
            for option in all_options:
                if (option.get_attribute("href") != None) and (option.get_attribute("href") not in array) and (
                        option.get_attribute("text").find('.') != -1):
                    array.append(option.get_attribute("href"))


    def add_skill(self, u):
        global skills
        driver.get(u)
        addsk = driver.find_element_by_id("Employee.ListsParent.ListsParent2.SkillList.addObjectSkillRelation")
        window_before = driver.window_handles[0]
        addsk.click()
        window_after = driver.window_handles[1]
        driver.switch_to_window(window_after)
        el = driver.find_element_by_id("htmlId")
        time.sleep(1)
        el.find_element_by_id("skill_outer").click()
        if self.comboBox_1.isVisible()==True:
            text = skills.get(self.comboBox_1.currentText())
            el.find_element_by_xpath('//a[@rel="' + text + '"]').click()
            elem = el.find_element_by_id("min-level")
            elem.clear()
            level = self.lineEdit_5.text()
            elem.send_keys(level)
            time.sleep(1)
            driver.find_element_by_id("add").click()
            driver.switch_to_window(window_before)

        else:
            text = self.lineEdit.text()
            selects = el.find_elements_by_tag_name('a')
            for select in selects:
                if (select.text.find(text) != -1) and (select.text != 'ОбучениеТранскомплекс (1 - 10)'):
                    text = str(select.text)
            el.find_element_by_xpath('//a[@title="' + text + '"]').click()
            elem = el.find_element_by_id("skill_box")
            elem.click()
            el.find_element_by_xpath('//a[@title="' + text + '"]').click()
            elem = el.find_element_by_id("min-level")
            elem.clear()
            level = self.lineEdit_5.text()
            elem.send_keys(level)
            time.sleep(1)
            driver.find_element_by_id("add").click()
            driver.switch_to_window(window_before)


    def change_profile(self, u):
        driver.get(u)
        chang = driver.find_element_by_id("Employee.ListsParent.ListsParent1.IASEmployeeCard.EditIASEmployee")
        window_before = driver.window_handles[0]
        chang.click()
        window_after = driver.window_handles[1]
        driver.switch_to_window(window_after)
        el = driver.find_element_by_id("htmlId")
        time.sleep(1)
        el.find_element_by_id("profile_outer").click()
        el.find_element_by_xpath('//a[@title="Оператор_Чер"]').click()
        time.sleep(1)
        driver.find_element_by_id("edit_outer").click()
        driver.switch_to_window(window_before)

    def change_profile_d(self,u):
        driver.get(u)
        chang = driver.find_element_by_id("Employee.ListsParent.ListsParent1.IASEmployeeCard.profile")
        if chang.text == 'Default profile':
            chang = driver.find_element_by_id("Employee.ListsParent.ListsParent1.IASEmployeeCard.EditIASEmployee")
            window_before = driver.window_handles[0]
            chang.click()
            window_after = driver.window_handles[1]
            driver.switch_to_window(window_after)
            el = driver.find_element_by_id("htmlId")
            time.sleep(1)
            el.find_element_by_id("profile_outer").click()
            prof=self.lineEdit.text()
            el.find_element_by_xpath('//a[@title="'+prof+'"]').click()
            time.sleep(1)
            driver.find_element_by_id("edit_outer").click()
            driver.switch_to_window(window_before)


    def delete_skill(self, u):
        driver.get(u)
        elem = driver.find_element_by_id("Employee.ListsParent.ListsParent2.SkillList")
        links = elem.find_elements_by_class_name("b-datatable__row")
        time.sleep(1)
        text = self.lineEdit.text()
        for link in links:
            el = link.find_element_by_tag_name("a").text
            if el == text:
                link.find_element_by_id("Employee.ListsParent.ListsParent2.SkillList.delete").click()
                break

    def tree (self):
        url = self.lineEdit_2.text()
        driver.get(url)
        elem = driver.find_elements_by_class_name("b-breadcrumbs__item")
        for u in elem:
            href = u.find_element_by_tag_name('a')
            if href.get_attribute("href").find('Organisations') == -1:
                array.append(str(href.get_attribute("href")))

    def add_sv(self,u):
        driver.get(u)
        time.sleep(1)
        window_before = driver.window_handles[0]
        driver.find_element_by_xpath('//a[@id="OU.OUMainCard.AddOUSupervisor"]').click()
        window_after = driver.window_handles[1]
        driver.switch_to_window(window_after)
        time.sleep(1)
        elem = driver.find_element_by_id("supervisor_search_str")
        newSV = self.lineEdit.text()
        elem.send_keys(newSV)
        driver.find_element_by_xpath('//i[@class="fa fa-search"]').click()
        time.sleep(1)
        driver.find_element_by_xpath('//a[@id="supervisor_box"]').click()
        driver.find_element_by_partial_link_text(newSV).click()
        driver.find_element_by_xpath('//button[@id="add"]').click()
        time.sleep(1)
        driver.switch_to_window(window_before)







#driver = webdriver.Firefox(executable_path=r"C:\Program Files\Mozilla Firefox\geckodriver.exe")
#driver.get("http://10.77.1.111:8080/")
#array = []
#start(driver)
#search_employee(driver)
#search_ou(driver)
#time.sleep(2)
#reaper(driver,array)
#add_skill(driver)
#delete_skill(driver)
#change_profile(driver)
#driver.close()

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = massshoting()
    window.show()
    app.exec_()

if __name__ == '__main__':
    main()