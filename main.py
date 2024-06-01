from lib_files import *

# Assuming "path" and "database" files contain the required paths and database details
with open("path_files/database") as f:
    database = f.read()
with open("path_files/path") as f:
    file_dict = f.read()
with open("path_files/report_path") as f:
    report_file_dict = f.read()
with open("path_files/AOI_Option") as f:
    AOI_option_file_dict = f.readlines()
with open("path_files/EOL_Option") as f:
    EOL_option_file_dict = f.readlines()
with open("path_files/employee_img") as f:
    image_folder_dict = f.read()

none_color = ("color: rgb(255, 255, 255);background-color: qlineargradient(spread:pad, x1:0.524118, y1:0, x2:0.671, "
              "y2:1, stop:0 #7f5a83, stop:1 #0d324d);")
color_set = "background-color: rgb(254, 122, 54);color: rgb(255, 255, 255); "
folder_path = ''
download_folder_path = ''
current_date = datetime.now().date().strftime("%Y/%m/%d")
current_time = datetime.now().time().strftime("%H:%M:%S")
current_month = datetime.now().strftime('%Y/%m')


# Generate Pdf include header and footer
class PDF(FPDF):
    def header(self):
        try:
            self.set_font('Arial', 'B', 33)
            self.cell(80)
            self.cell(30, 10, 'AOI PERSONAL REPORT', align='C')
            self.ln(20)
        except Exception as e:
            print(e)

    def footer(self):
        try:
            self.set_y(-15)
            self.set_font('Arial', 'I', 8)
            self.cell(0, 10, 'Page ' + str(self.page_no()) + '/{nb}', 0, 0, 'C')
        except Exception as e:
            print(e)

class MplCanvas(FigureCanvas):
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig, self.ax = plt.subplots(figsize=(width, height), dpi=dpi)
        super().__init__(fig)


class LabeledLineEdit(QWidget):
    def __init__(self, label_text):
        super().__init__()
        layout = QHBoxLayout()
        self.label = QLabel(label_text)
        self.line_edit = QLineEdit()
        layout.addWidget(self.label)
        layout.addWidget(self.line_edit)
        self.setLayout(layout)

    def text(self):
        return self.line_edit.text()


font = QFont()
font.setPointSize(14)
font.bold()


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.next_window = None
        self.login_window = None
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("Main Window")
        UIFunctions.removeTitleBar(False)
        startSize = QSize(1000, 720)
        self.resize(startSize)
        self.setMinimumSize(startSize)
        self.ui.btn_toggle_menu.clicked.connect(lambda: UIFunctions.toggleMenu(self, 50, True))
        self.ui.stackedWidget.setMinimumWidth(20)
        UIFunctions.selectStandardMenu(self, "btn_status")
        self.ui.frame_left_menu.hide()
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_about)
        UIFunctions.userIcon(self, "User", "", True)

        def Movewindow(event):
            if UIFunctions.returStatus() == 1:
                UIFunctions.maximize_restore(self)
            if event.buttons() == Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.dragPos)
                self.dragPos = event.globalPos()
                event.accept()

        self.ui.frame_label_top_btns.mouseMoveEvent = Movewindow
        UIFunctions.uiDefinitions(self)
        self.ui.btn_maximize_restore.click()
        self.ui.bt_take_test.clicked.connect(self.confirm)
        self.ui.btn_test.clicked.connect(self.login_option_changed)
        self.ui.btn_login.clicked.connect(self.take_test_option_changed)
        # Search Box
        self.ui.search_field.textChanged.connect(self.filter_combobox)
        # Test Option Box
        folder = os.listdir(file_dict)
        for file in folder:
            self.ui.comboBox.addItem(file)
        self.ui.btn_test_2.hide()
        self.ui.btn_test_3.hide()
        self.ui.btn_test_4.hide()
        self.ui.btn_test_5.hide()
        self.ui.btn_logout.hide()
        self.ui.password_field.setEchoMode(QLineEdit.Password)
        self.ui.pushButton_3.clicked.connect(self.submit)
        self.ui.pushButton_9.clicked.connect(self.login)


    def confirm(self):
        self.ui.frame_left_menu.show()
        self.ui.btn_test.show()
        self.ui.btn_test.setStyleSheet(
            "QPushButton{color: rgb(255, 255, 255);background-color: qlineargradient(spread:pad, x1:0.524118, "
            "y1:0, x2:0.671, y2:1, stop:0 #7f5a83, stop:1 #0d324d);padding: 5px 7px;}QPushButton:hover "
            "{background-color: rgb(44, 49, 60)}QPushButton:pressed {	background-color: rgb(44, 49, 60);color: "
            "rgb(6, 6, 6);}")

    def login_option_changed(self):
        # Login Page
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_test)

    def take_test_option_changed(self):
        # Take Test
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_login)

    def filter_combobox(self, text):
        try:
            self.ui.comboBox.clear()
            folder = os.listdir(file_dict)
            filtered_items = [item for item in folder if text.lower() in item.lower()]
            self.ui.comboBox.addItems(filtered_items)
        except Exception as e:
            print(e)

    def login(self):
        try:
            username = self.ui.user_name_field.text()
            password = self.ui.password_field.text()
            if username == "ad" and password == "ad":
                self.login_window = AdminWindow(username, password, self)
                self.login_window.show()
                self.hide()
            else:
                QMessageBox.warning(self, "Warning", "Please Enter Correct User Name and Password")
        except Exception as e:
            print(e)

    def read_images_from_folder(self, folder_path_loc):
        try:
            images = []
            for filename in os.listdir(folder_path_loc):
                if filename.endswith('.jpg') or filename.endswith('.png') or filename.endswith(
                        '.mp4'):  # Adjust extensions as needed
                    images.append(filename)
            return images
        except Exception as e:
            print(e)

    def submit(self):
        try:
            option = self.ui.comboBox.currentText()
            user_input = self.ui.input_field.text().strip()
            conn = sqlite3.connect(database)
            cur = conn.cursor()
            personal_details = cur.execute('SELECT * FROM personal_details WHERE Emp_id=?', (user_input,)).fetchall()
            exam_details = cur.execute('SELECT * FROM exam_details WHERE employee_id = ? AND date = ?',
                                       (user_input, current_date)).fetchall()
            conn.commit()
            conn.close()
            if exam_details:
                QMessageBox.warning(self, "Warning", "Exam already submitted.", QMessageBox.Ok)
            else:
                option_selected = file_dict + '/' + option
                selected_option = self.read_images_from_folder(option_selected)
                if option and user_input:
                    if personal_details:
                        self.next_window = ExamWindow(option, user_input, selected_option, personal_details, self)
                        self.next_window.show()
                        self.hide()
                    else:
                        QMessageBox.warning(self, "Warning", "Please enter your correct Employee ID")
                else:
                    QMessageBox.warning(self, "Warning", "Both option and input must be filled!")
        except Exception as e:
            print(e)


class ExamWindow(QMainWindow):
    def __init__(self, option, user_input, option_selected, personal_details, main_window):
        QMainWindow.__init__(self)
        self.video_capture = None
        self.setWindowTitle("Next Window")
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        UIFunctions.removeTitleBar(False)
        startSize = QSize(1000, 720)
        self.resize(startSize)
        self.setMinimumSize(startSize)
        self.ui.btn_toggle_menu.clicked.connect(lambda: UIFunctions.toggleMenu(self, 50, True))
        self.ui.stackedWidget.setMinimumWidth(20)
        UIFunctions.selectStandardMenu(self, "btn_status")

        def Movewindow(event):
            if UIFunctions.returStatus() == 1:
                UIFunctions.maximize_restore(self)
            if event.buttons() == Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.dragPos)
                self.dragPos = event.globalPos()
                event.accept()

        self.ui.frame_label_top_btns.mouseMoveEvent = Movewindow
        UIFunctions.uiDefinitions(self)
        self.ui.frame_left_menu.hide()
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_exam)

        self.ui.btn_maximize_restore.click()
        self.ui.btn_maximize_restore.click()
        self.main_window = main_window
        self.details = (option, user_input, option_selected, personal_details)
        self.ui.display_label_model_name.setText(option)
        for detail in personal_details:
            self.ui.display_label_name.setText(detail[1])
            self.ui.display_label_name.setFont(font)
            self.ui.display_label_dep.setText(detail[2])
            self.ui.display_label_dep.setFont(font)
        self.total_question = str(len(option_selected))
        self.ui.display_label_question.setText(self.total_question)
        self.ui.display_label_question.setFont(font)
        self.ui.pushButton_4.hide()
        self.ui.btn_close.hide()
        self.ui.btn_minimize.hide()
        self.ui.btn_maximize_restore.hide()

        self.answer_store = {}
        self.ui.pushButton_3.hide()
        self.test_option_buttons = []
        for option_text in option_selected:
            test_option_button = QPushButton(option_text.split('_')[0])
            test_option_button.setToolTip(option_text)  # Set full detail as tooltip
            self.ui.verticalLayout_14.addWidget(test_option_button)
            self.test_option_buttons.append(test_option_button)  # Add button to the list
        # Connect the clicked signal of each button to the selected_option method
        for button in self.test_option_buttons:
            button.clicked.connect(self.selected_option)
        if option.split('_')[0] == 'AOI':
            for option in AOI_option_file_dict:
                self.ui.comboBox_3.addItem(option.strip())
        if option.split('_')[0] == 'EOL':
            for option in EOL_option_file_dict:
                self.ui.comboBox_3.addItem(option.strip())
        self.ui.comboBox_3.hide()
        self.ui.pushButton_2.hide()
        self.ui.comboBox_3.currentIndexChanged.connect(self.update_combo_selection)
        self.ui.pushButton_4.clicked.connect(self.test_submit)
        self.show()

    def update_combo_selection(self, index):
        try:
            if self.clicked_button:
                option_text = self.ui.comboBox_3.currentText()
                if "ng" in self.answer_store.get(self.clicked_button.text(), ""):
                    self.answer_store[self.clicked_button.text()] = f"ng_{option_text}"
                self.update_color()
        except Exception as e:
            print(f"Error in update_combo_selection: {e}")

    def selected_option(self):
        try:
            self.clicked_button = self.sender()
            self.ui.label_title_bar_top_4.setText(self.clicked_button.text())
            if self.clicked_button:
                full_option_text = self.clicked_button.toolTip()
                path_end_file = full_option_text.endswith('.mp4')
                self.ui.good_button.setStyleSheet(none_color)
                self.ui.ng_button.setStyleSheet(none_color)
                self.ui.comboBox_3.hide()
                self.ui.good_button.clicked.connect(self.answer_clicked)
                self.ui.ng_button.clicked.connect(self.answer_clicked)
                self.update_color()
                if path_end_file:
                    video_path = file_dict + "/" + self.details[0] + "/" + full_option_text
                    self.video_capture = cv2.VideoCapture(video_path)
                    self.play_video()
                else:
                    image_path = file_dict + "/" + self.details[0] + "/" + full_option_text
                    self.pixmap = QPixmap(image_path)
                    if not self.pixmap.isNull():
                        self.ui.image_label.setPixmap(self.pixmap)
        except Exception as e:
            print(f"Error in selected_option: {e}")

    def play_video(self):
        if self.video_capture and self.video_capture.isOpened():
            ret, frame = self.video_capture.read()
            if ret:
                rgb_image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                h, w, ch = rgb_image.shape
                bytes_per_line = ch * w
                qt_image = QImage(rgb_image.data, w, h, bytes_per_line, QImage.Format_RGB888)
                self.pixmap = QPixmap.fromImage(qt_image)
                self.ui.image_label.setPixmap(self.pixmap)
                self.ui.image_label.setScaledContents(True)
                QTimer.singleShot(33, self.play_video)  # approximately 30 FPS
            else:
                self.video_capture.release()

    def update_color(self):
        try:
            if self.answer_store:
                for key, values in self.answer_store.items():
                    if values.split('_')[0] == 'good' and self.clicked_button.text() == key:
                        self.ui.good_button.setStyleSheet(color_set)
                        self.ui.ng_button.setStyleSheet(none_color)
                        self.ui.comboBox_3.hide()
                    if values.split('_')[0] == 'ng' and self.clicked_button.text() == key:
                        self.ui.ng_button.setStyleSheet(color_set)
                        self.ui.good_button.setStyleSheet(none_color)
                        self.ui.comboBox_3.show()
                        self.ui.comboBox_3.setCurrentText(values.split('_')[1])
        except Exception as e:
            print(e)

    #
    def answer_clicked(self):
        try:
            if self.clicked_button:
                if self.sender().text() == "good":
                    self.ui.comboBox_3.hide()
                    self.ui.comboBox_3.close()
                    self.clicked_button.setStyleSheet(color_set)
                    sub_option = '_'.join((self.sender().text(), 'none'))
                if self.sender().text() == "ng":
                    self.ui.comboBox_3.show()
                    self.clicked_button.setStyleSheet(color_set)
                    sub_option = '_'.join((self.sender().text(), self.ui.comboBox_3.currentText()))
                self.answer_store[self.clicked_button.text()] = sub_option
                self.update_color()
                if str(len(self.answer_store)) == self.total_question:
                    self.ui.pushButton_4.show()
        except Exception as e:
            print(e)

    def test_submit(self):
        try:
            confirmation = QMessageBox.question(self, "Confirmation", "Are you sure you want to submit the test?",
                                                QMessageBox.Yes | QMessageBox.No)
            if confirmation == QMessageBox.Yes:
                data = self.answer_store
                if data:
                    total_question = len(data)
                    score_count = 0
                    marks = {}
                    incorrect_answers_question = {}
                    for i, j in data.items():
                        for img in self.details[2]:
                            if (img.split('_')[0] == i and img.split('_')[1] == j.split('_')[0] and
                                    img.split('_')[2] == j.split('_')[1]):
                                marks[i] = j
                                score_count += 1
                    for key in data:
                        if key in marks and data[key] == marks[key]:
                            pass
                        else:
                            incorrect_answers_question[key] = data[key]
                    test_score = (score_count, total_question)
                    incorrect_answers = [ques for ques in incorrect_answers_question.keys()]
                    incorrect_question = [ans for ans in incorrect_answers_question.values()]
                    self.submit_window = ScoreWindow(test_score, self.details, self.main_window,
                                                     incorrect_answers, incorrect_question)
                    self.submit_window.show()
                    self.hide()
        except Exception as e:
            print(e)


class ScoreWindow(QMainWindow):
    def __init__(self, score, user_details, main_window, incorrect_question, incorrect_answer):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        UIFunctions.removeTitleBar(False)
        startSize = QSize(1000, 720)
        self.resize(startSize)
        self.setMinimumSize(startSize)
        self.ui.btn_toggle_menu.clicked.connect(lambda: UIFunctions.toggleMenu(self, 50, True))
        self.ui.stackedWidget.setMinimumWidth(20)
        UIFunctions.selectStandardMenu(self, "btn_status")

        def Movewindow(event):
            if UIFunctions.returStatus() == 1:
                UIFunctions.maximize_restore(self)
            if event.buttons() == Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.dragPos)
                self.dragPos = event.globalPos()
                event.accept()

        self.ui.frame_label_top_btns.mouseMoveEvent = Movewindow
        UIFunctions.uiDefinitions(self)
        self.ui.frame_left_menu.hide()
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_score)

        self.ui.btn_maximize_restore.click()
        self.ui.btn_maximize_restore.click()
        self.main_window = main_window

        self.detail = [detail for _ in user_details[3] for detail in _]
        self.correct_answers, self.total_questions = score[0], score[1]
        self.Pass_Percentage = int((self.correct_answers / self.total_questions) * 100)
        self.status = ("pass" if self.Pass_Percentage >= 50 else 'fail')
        self.ui.employee_name_label.setText(self.detail[1])
        self.ui.employee_name_label.setFont(font)
        self.ui.employee_id_label.setText(self.detail[0])
        self.ui.employee_id_label.setFont(font)
        self.ui.dep_label_2.setText(self.detail[2])
        self.ui.dep_label_2.setFont(font)

        self.incorrect_question = json.dumps(incorrect_question)
        self.incorrect_answer = json.dumps(incorrect_answer)
        self.user_details = user_details
        self.ui.status_label.setText(self.status)
        self.ui.status_label.setFont(font)
        self.ui.score_label.setNum(self.correct_answers)
        self.ui.score_label.setFont(font)
        self.ui.percentage_label.setNum(self.Pass_Percentage)
        self.ui.percentage_label.setFont(font)
        self.ui.total_ques_label.setNum(self.total_questions)
        self.ui.total_ques_label.setFont(font)
        self.insert_data_base()
        self.write_report()
        self.ui.btn_close.hide()
        self.ui.btn_minimize.hide()
        self.ui.btn_maximize_restore.hide()
        self.ui.submit_bts.clicked.connect(self.go_back)

    def go_back(self):
        self.main_window.show()
        self.close()

    def insert_data_base(self):
        try:
            conn = sqlite3.connect(database)
            cur = conn.cursor()
            column_names = ('name, employee_id, department, model, date, score, percentage, status,'
                            ' incorrect_answer, total_question, time, incorrect_question')
            insert_values = (self.detail[1], self.detail[0], self.detail[2], self.user_details[0], current_date,
                             self.correct_answers, self.Pass_Percentage, self.status, self.incorrect_answer,
                             self.total_questions, current_time, self.incorrect_question)
            cur.execute(
                'INSERT INTO exam_details ({}) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'.format(column_names),
                insert_values)
            conn.commit()
            conn.close()
        except Exception as e:
            print(e)

    def write_report(self):
        try:
            value_fetch = ('name,employee_id,department,model,date,score,percentage,status,incorrect_answer,'
                           'incorrect_question,time')
            conn = sqlite3.connect(database)
            cur = conn.cursor()
            report_dt = cur.execute('select {} from exam_details where employee_id=? AND date = ?'.format(value_fetch),
                                    (self.detail[0], current_date)).fetchone()
            conn.commit()
            conn.close()
            self.report_details = [report for report in report_dt]
            labels = ["Employee ID", "Employee Name", "Department", "Model", "Date",
                      "Score", "Percentage", "Status"]
            names = self.report_details
            image = []
            folder = os.listdir(file_dict)
            for file in folder:
                if self.report_details[3] in file:
                    img_path = os.listdir(file_dict + file)
                    for img in img_path:
                        if img.split('_')[0] in json.loads(self.report_details[9]):
                            image.append(file_dict + file + '/' + img)
            pdf = PDF()
            pdf.alias_nb_pages()
            pdf.add_page()
            pdf.set_font('Times', '', 18)
            for sn, label in enumerate(labels):
                pdf.cell(0, 20, (label + " : " + names[sn]), 0, 4)
            employee_image_jpg = os.path.join(image_folder_dict, f'{self.detail[0]}.jpg')
            employee_image_png = os.path.join(image_folder_dict, f'{self.detail[0]}.png')
            default_image_path = os.path.join(image_folder_dict, 'noimage.png')
            print(image_folder_dict)
            # Check if the employee's image file (JPEG) exists
            if os.path.exists(employee_image_jpg):
                # If the JPEG image exists, assign its path to a variable
                image_path = employee_image_jpg
            # Check if the employee's image file (PNG) exists
            elif os.path.exists(employee_image_png):
                # If the PNG image exists, assign its path to a variable
                image_path = employee_image_png
            else:
                # If neither JPEG nor PNG image exists, load a default image
                image_path = default_image_path
            print(image_path)
            pdf.image(image_path, x=120, y=40, w=40)
            pdf.add_page()
            if self.report_details:
                incorrect_questions = json.loads(self.report_details[9])
                incorrect_answers = json.loads(self.report_details[8])
                image_paths = image
                table_data_insert = tuple(zip(incorrect_questions, incorrect_answers, image_paths,
                                              ['_'.join(os.path.basename(path).split('_')[1:3]) for path in image_paths]))
            else:
                table_data_insert = ()
            data_label = ("Incorrect Question", "User Answer", "Image", "Correct Answer")
            TABLE_DATA = (data_label,) + table_data_insert
            cell_width = 49
            cell_height = 30
            for header in TABLE_DATA[0]:
                pdf.cell(cell_width, cell_height, header, border=1)
            pdf.ln(cell_height)
            for row in TABLE_DATA[1:]:
                for i, item in enumerate(row):
                    if i == 2:
                        pdf.cell(cell_width, cell_height, border=1)
                        x = pdf.get_x() - cell_width
                        y = pdf.get_y()
                        os.makedirs("extract_frame", exist_ok=True)
                        image_path = 'extract_frame/extract_frame.jpg'
                        if os.path.basename(item).split('.')[1] == 'mp4':
                            cap = cv2.VideoCapture(item)
                            if not cap.isOpened():
                                print("Error: Could not open video.")
                                exit()
                            frame_number = 2
                            cap.set(cv2.CAP_PROP_POS_FRAMES, frame_number - 1)  # Frame numbers are 0-based in OpenCV
                            ret, frame = cap.read()
                            if not ret:
                                print(f"Error: Could not read frame number {frame_number}.")
                            else:
                                cv2.imwrite(image_path, frame)
                            cap.release()
                            pdf.image(image_path, x=x + 5, y=y + 5, w=cell_width - 10, h=cell_height - 10)
                            print('mp4')
                        else:
                            pdf.image(item, x=x + 5, y=y + 5, w=cell_width - 10, h=cell_height - 10)
                    else:
                        pdf.cell(cell_width, cell_height, item, border=1)
                pdf.ln(cell_height)
            report_change_date = ''.join(self.report_details[4].split('/'))
            report_change_time = ''.join(self.report_details[10].split(':'))
            full_path = (report_file_dict + self.report_details[1] +
                         '_' + report_change_date + '_' + report_change_time + '_' + self.report_details[
                             3] + '_' + "REPORT.pdf")
            pdf.output(full_path, 'F')
        except Exception as e:
            print(e)


class AdminWindow(QMainWindow):
    def __init__(self, option, user_input, main_window):
        QMainWindow.__init__(self)
        self.add_model_window = None
        self.report_window = None
        self.edit_model_window = None
        self.create_account_window = None
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("Admin Window")
        UIFunctions.removeTitleBar(False)
        startSize = QSize(1000, 720)
        self.resize(startSize)
        self.setMinimumSize(startSize)
        self.ui.btn_toggle_menu.clicked.connect(lambda: UIFunctions.toggleMenu(self, 50, True))
        self.ui.stackedWidget.setMinimumWidth(20)
        UIFunctions.selectStandardMenu(self, "btn_status")
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_admin)
        UIFunctions.userIcon(self, "User", "", True)
        self.ui.stackedWidget.setMinimumWidth(20)
        UIFunctions.selectStandardMenu(self, "btn_status")
        self.ui.btn_test.hide()
        self.ui.btn_login.hide()

        def Movewindow(event):
            if UIFunctions.returStatus() == 1:
                UIFunctions.maximize_restore(self)
            if event.buttons() == Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.dragPos)
                self.dragPos = event.globalPos()
                event.accept()

        self.ui.frame_label_top_btns.mouseMoveEvent = Movewindow
        UIFunctions.uiDefinitions(self)
        self.ui.btn_maximize_restore.click()
        self.ui.btn_maximize_restore.click()
        self.main_window = main_window
        self.ui.label_user_icon.setText('Admin')
        self.ui.btn_test_2.show()
        self.ui.btn_test_3.show()
        self.ui.btn_test_4.hide()
        self.ui.btn_test_5.show()
        self.ui.btn_test_3.clicked.connect(self.create_account)
        self.ui.btn_test_5.clicked.connect(self.add_model)
        self.ui.btn_test_4.clicked.connect(self.edit_model)
        self.ui.btn_test_2.clicked.connect(self.view_report)
        self.ui.btn_logout.clicked.connect(self.go_back)

    def go_back(self):
        self.main_window.show()
        self.close()

    def create_account(self):
        self.create_account_window = CreateAccountWindow(self.main_window)
        self.create_account_window.show()
        self.hide()

    def add_model(self):
        self.add_model_window = AddModelWindow(self.main_window)
        self.add_model_window.show()
        self.hide()

    def edit_model(self):
        self.edit_model_window = EditModelWindow(self.main_window)
        self.edit_model_window.show()
        self.hide()

    def view_report(self):
        self.report_window = ViewReportWindow(self.main_window)
        self.report_window.show()
        self.hide()


class ViewReportWindow(QMainWindow):
    def __init__(self, main_window):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("Report Window")
        UIFunctions.removeTitleBar(False)
        startSize = QSize(1000, 720)
        self.resize(startSize)
        self.setMinimumSize(startSize)
        self.ui.btn_toggle_menu.clicked.connect(lambda: UIFunctions.toggleMenu(self, 50, True))
        self.ui.stackedWidget.setMinimumWidth(20)
        UIFunctions.selectStandardMenu(self, "btn_status")
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_report)
        UIFunctions.userIcon(self, "User", "", True)
        self.ui.stackedWidget.setMinimumWidth(20)
        UIFunctions.selectStandardMenu(self, "btn_status")
        self.ui.btn_test.hide()
        self.ui.btn_login.hide()
        self.ui.btn_test_4.hide()

        def Movewindow(event):
            if UIFunctions.returStatus() == 1:
                UIFunctions.maximize_restore(self)
            if event.buttons() == Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.dragPos)
                self.dragPos = event.globalPos()
                event.accept()

        self.ui.frame_label_top_btns.mouseMoveEvent = Movewindow
        UIFunctions.uiDefinitions(self)
        self.ui.btn_maximize_restore.click()
        self.ui.btn_maximize_restore.click()
        self.main_window = main_window
        self.layout = QVBoxLayout()
        self.canvas = MplCanvas(self, width=5, height=4, dpi=100)
        self.layout.addWidget(self.canvas)
        self.ui.pushButton_6.clicked.connect(self.report_button)
        self.ui.btn_logout.clicked.connect(self.go_back)
        self.ui.btn_test_3.clicked.connect(self.create_account)
        self.ui.btn_test_5.clicked.connect(self.add_model)
        self.ui.btn_test_4.clicked.connect(self.edit_model)
        self.ui.btn_test_2.clicked.connect(self.view_report)
        self.ui.btn_logout.clicked.connect(self.go_back)

    def go_back(self):
        self.main_window.show()
        self.close()

    def create_account(self):
        self.create_account_window = CreateAccountWindow(self.main_window)
        self.create_account_window.show()
        self.hide()

    def add_model(self):
        self.add_model_window = AddModelWindow(self.main_window)
        self.add_model_window.show()
        self.hide()

    def edit_model(self):
        self.edit_model_window = EditModelWindow(self.main_window)
        self.edit_model_window.show()
        self.hide()

    def view_report(self):
        self.report_window = ViewReportWindow(self.main_window)
        self.report_window.show()
        self.hide()

    def report_button(self):
        try:
            report_search = self.ui.lineEdit_2.text()
            report_folder = os.listdir(report_file_dict)
            report_fetch_details = [report for report in report_folder if report_search in report]
            if report_fetch_details:
                for file in report_fetch_details:  # Changed report_folder to report_fetch_details
                    path = ' '.join((file.split('_')[0], (
                        '-'.join((file.split('_')[1][:4], file.split('_')[1][4:6], file.split('_')[1][6:])))))
                    self.ui.comboBox_2.addItem(path)
                    self.ui.comboBox_2.setToolTip(file)
                self.ui.bt_report.clicked.connect(self.open_pdf)
                self.ui.bt_report_2.clicked.connect(self.graphical_report_)
            else:
                QMessageBox.warning(self, "Warning", "Please enter correct Employee ID")
        except Exception as e:
            print(e)

    def graphical_report_(self):
        try:
            report_search = self.ui.lineEdit_2.text()
            if report_search:
                conn = sqlite3.connect(database)
                cur = conn.cursor()
                graphical_details = cur.execute('SELECT * FROM exam_details where employee_id = ? or model=? ',
                                                (report_search, report_search)).fetchone()
                if graphical_details:
                    employee_details = cur.execute(
                        'SELECT date,model,percentage FROM exam_details where employee_id = ? ',
                        (report_search,)).fetchall()
                    if employee_details:
                        employee_details = [entry for entry in employee_details if entry[0].startswith(current_month)]
                        self.ui.graph_widget.setLayout(self.layout)
                        self.plot(employee_details)
                else:
                    QMessageBox.warning(self, "Warning", "Please enter correct Employee ID")
        except Exception as e:
            print(e)

    def open_pdf(self):
        try:
            option = self.ui.comboBox_2.toolTip()
            os.startfile(os.path.join(report_file_dict, option))
            self.ui.comboBox_2.clear()
        except Exception as e:
            print(e)

    def plot(self, data):
        dates = [entry[0] for entry in data]
        models = [entry[1] for entry in data]
        scores = [int(entry[2]) for entry in data]
        self.canvas.ax.bar(dates, scores)
        for i, score in enumerate(scores):
            value = ','.join((str(models[i]), str(score)))
            self.canvas.ax.text(i, score + 0.4, value, ha='center')
        self.canvas.ax.set_xlabel('Date')
        self.canvas.ax.set_ylabel('Score')
        self.canvas.ax.set_title('Scores by Date and Model')
        self.canvas.ax.figure.tight_layout()
        self.canvas.draw()



class CreateAccountWindow(QMainWindow):
    def __init__(self, main_window):
        QMainWindow.__init__(self)
        self.video_capture = None
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("Add Model Window")
        UIFunctions.removeTitleBar(False)
        startSize = QSize(1000, 720)
        self.resize(startSize)
        self.setMinimumSize(startSize)
        self.ui.btn_toggle_menu.clicked.connect(lambda: UIFunctions.toggleMenu(self, 50, True))
        self.ui.stackedWidget.setMinimumWidth(20)
        UIFunctions.selectStandardMenu(self, "btn_status")
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_adduser)
        UIFunctions.userIcon(self, "User", "", True)
        self.ui.stackedWidget.setMinimumWidth(20)
        UIFunctions.selectStandardMenu(self, "btn_status")
        self.ui.btn_test.hide()
        self.ui.btn_login.hide()
        self.ui.btn_test_4.hide()

        def Movewindow(event):
            if UIFunctions.returStatus() == 1:
                UIFunctions.maximize_restore(self)
            if event.buttons() == Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.dragPos)
                self.dragPos = event.globalPos()
                event.accept()

        self.ui.frame_label_top_btns.mouseMoveEvent = Movewindow
        UIFunctions.uiDefinitions(self)
        self.ui.btn_maximize_restore.click()
        self.ui.btn_maximize_restore.click()
        self.main_window = main_window
        self.setWindowTitle("Create Account Window")
        self.main_window = main_window
        self.layout = QVBoxLayout()
        self.ui.btn_logout.clicked.connect(self.go_back)
        self.ui.pushButton_10.clicked.connect(self.create_account_submit)
        self.ui.btn_test_3.clicked.connect(self.create_account)
        self.ui.btn_test_5.clicked.connect(self.add_model)
        self.ui.btn_test_4.clicked.connect(self.edit_model)
        self.ui.btn_test_2.clicked.connect(self.view_report)
        self.ui.btn_logout.clicked.connect(self.go_back)

    def go_back(self):
        self.main_window.show()
        self.close()

    def create_account(self):
        self.create_account_window = CreateAccountWindow(self.main_window)
        self.create_account_window.show()
        self.hide()

    def add_model(self):
        self.add_model_window = AddModelWindow(self.main_window)
        self.add_model_window.show()
        self.hide()

    def edit_model(self):
        self.edit_model_window = EditModelWindow(self.main_window)
        self.edit_model_window.show()
        self.hide()

    def view_report(self):
        self.report_window = ViewReportWindow(self.main_window)
        self.report_window.show()
        self.hide()

    def create_account_submit(self):
        try:
            details = self.ui.user_name_field_2.text(), self.ui.employeeID_field.text(), self.ui.department_field.text()
            if self.ui.user_name_field_2.text() and self.ui.employeeID_field.text() and self.ui.department_field.text():
                conn = sqlite3.connect(database)
                cur = conn.cursor()
                check_detail = cur.execute('select Emp_id from personal_details where Emp_id= ?',
                                           (details[1],)).fetchone()
                if not check_detail:
                    cur.execute('insert into personal_details ( Name,Emp_id, Dep) values (?,?,?)', details)
                    conn.commit()
                    conn.close()
                    QMessageBox.information(self, 'Account Created Successfully', 'Account created successfully!')
                    self.ui.user_name_field_2.clear()
                    self.ui.employeeID_field.clear()
                    self.ui.department_field.clear()
                else:
                    QMessageBox.warning(self, 'Warning', 'Employee details already exists')
            else:
                QMessageBox.warning(self, 'Warning', 'Please enter correct Username and Department')
        except Exception as e:
            print(e)

    def go_back(self):
        self.main_window.show()
        self.close()


class AddModelWindow(QMainWindow):
    def __init__(self, main_window):
        QMainWindow.__init__(self)
        self.video_capture = None
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.btn_test.hide()
        self.ui.btn_login.hide()
        self.ui.btn_test_4.hide()
        self.setWindowTitle("Add Model Window")
        UIFunctions.removeTitleBar(False)
        startSize = QSize(1000, 720)
        self.resize(startSize)
        self.setMinimumSize(startSize)
        self.ui.btn_toggle_menu.clicked.connect(lambda: UIFunctions.toggleMenu(self, 50, True))
        self.ui.stackedWidget.setMinimumWidth(20)
        UIFunctions.selectStandardMenu(self, "btn_status")
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_model)
        UIFunctions.userIcon(self, "User", "", True)
        self.ui.stackedWidget.setMinimumWidth(20)
        UIFunctions.selectStandardMenu(self, "btn_status")


        def Movewindow(event):
            if UIFunctions.returStatus() == 1:
                UIFunctions.maximize_restore(self)
            if event.buttons() == Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.dragPos)
                self.dragPos = event.globalPos()
                event.accept()

        self.ui.frame_label_top_btns.mouseMoveEvent = Movewindow
        UIFunctions.uiDefinitions(self)
        self.ui.btn_maximize_restore.click()
        self.ui.btn_maximize_restore.click()
        self.main_window = main_window
        self.ui.pushButton_7.hide()
        self.ui.good_button_2.hide()
        self.ui.pushButton.hide()
        self.ui.ng_button_2.hide()
        self.ui.comboBox_4.hide()
        self.ui.pushButton_8.hide()
        self.ui.pushButton_5.hide()
        self.total_question = ''

        self.ui.label_name_2.setFont(font)
        self.ui.pushButton_7.clicked.connect(self.select_folder)
        self.ui.pushButton.clicked.connect(self.on_left_button_clicked)
        self.right_side_button = QPushButton(">", self)
        self.ui.pushButton_8.clicked.connect(self.on_right_button_clicked)
        self.ui.label_newmodelname.textChanged.connect(self.check_input)
        self.value_store = {}
        self.current_image_index = 0
        self.img_loc = ''
        self.ui.btn_test_3.clicked.connect(self.create_account)
        self.ui.btn_test_5.clicked.connect(self.add_model)
        self.ui.btn_test_4.clicked.connect(self.edit_model)
        self.ui.btn_test_2.clicked.connect(self.view_report)
        self.ui.btn_logout.clicked.connect(self.go_back)

    def go_back(self):
        self.main_window.show()
        self.close()

    def create_account(self):
        self.create_account_window = CreateAccountWindow(self.main_window)
        self.create_account_window.show()
        self.hide()

    def add_model(self):
        self.add_model_window = AddModelWindow(self.main_window)
        self.add_model_window.show()
        self.hide()

    def edit_model(self):
        self.edit_model_window = EditModelWindow(self.main_window)
        self.edit_model_window.show()
        self.hide()

    def view_report(self):
        self.report_window = ViewReportWindow(self.main_window)
        self.report_window.show()
        self.hide()

    def check_input(self):
        if self.ui.label_newmodelname.text().split('_')[0] == 'AOI':
            self.ui.pushButton_7.show()
            for option in AOI_option_file_dict:
                self.ui.comboBox_4.addItem(option.strip())
        elif self.ui.label_newmodelname.text().split('_')[0] == 'EOL':
            self.ui.pushButton_7.show()
            for option in EOL_option_file_dict:
                self.ui.comboBox_4.addItem(option.strip())
        else:
            self.ui.pushButton_7.hide()
            self.ui.good_button_2.hide()
            self.ui.ng_button_2.hide()
            self.ui.comboBox_4.hide()

    def select_folder(self):
        try:
            global folder_path
            options = QFileDialog.Options()
            folder_path = QFileDialog.getExistingDirectory(self, "Select Folder", options=options)
            self.ui.comboBox_4.currentIndexChanged.connect(self.update_combo_selection)
            if folder_path:
                self.ui.lab_selected.setText(folder_path)
                self.display_image()
                self.ui.pushButton_5.clicked.connect(self.add_model_submit_button)
        except Exception as e:
            print(e)

    def on_left_button_clicked(self):
        try:
            if self.current_image_index > 0:
                self.current_image_index -= 1
                self.display_image()
            if self.current_image_index < int(self.total_question) - 1:
                self.ui.pushButton_8.show()
        except Exception as e:
            print(e)

    def on_right_button_clicked(self):
        try:
            global folder_path
            folder_path = self.ui.lab_selected.text()
            images = [filename for filename in os.listdir(folder_path) if
                      filename.endswith(('.jpg', '.jpeg', '.png', '.gif', '.bmp', '.mp4'))]
            if self.current_image_index < len(images) - 1:
                self.current_image_index += 1
                self.display_image()
            if self.current_image_index >= int(self.total_question) - 1:
                self.ui.pushButton_8.hide()
        except Exception as e:
            print(e)

    def display_image(self):
        try:
            global folder_path
            folder_path = self.ui.lab_selected.text()
            images = [filename for filename in os.listdir(folder_path) if
                      filename.endswith(('.jpg', '.jpeg', '.png', '.gif', '.bmp', '.mp4'))]
            self.total_question = str(len(images))
            current_question = str(self.current_image_index + 1) + "/" + self.total_question
            self.ui.label_name_2.setText(current_question)
            self.ui.good_button_2.show()
            self.ui.ng_button_2.show()
            self.ui.pushButton.show()
            self.ui.pushButton_8.show()
            if images:
                image_path = os.path.join(folder_path, images[self.current_image_index])
                self.img_loc = [os.path.join(folder_path, img) for img in images]
                if image_path.endswith('.mp4'):
                    self.video_capture = cv2.VideoCapture(image_path)
                    self.play_video()
                else:
                    pixmap = QPixmap(image_path)
                    self.ui.image_label_2.setPixmap(pixmap)
                self.ui.good_button_2.setStyleSheet(none_color)
                self.ui.ng_button_2.setStyleSheet(none_color)
                self.update_add_model_color()
                self.ui.good_button_2.clicked.connect(self.add_model_selected_button)
                self.ui.ng_button_2.clicked.connect(self.add_model_selected_button)
        except Exception as e:
            print(e)

    def update_add_model_color(self):
        try:
            if self.value_store:
                for key, values in self.value_store.items():
                    if values.split('_')[0] == 'good' and (self.current_image_index + 1) == key:
                        self.ui.good_button_2.setStyleSheet(color_set)
                        self.ui.ng_button_2.setStyleSheet(none_color)
                        self.ui.comboBox_4.hide()
                    if values.split('_')[0] == 'ng' and (self.current_image_index + 1) == key:
                        self.ui.ng_button_2.setStyleSheet(color_set)
                        self.ui.good_button_2.setStyleSheet(none_color)
                        self.ui.comboBox_4.show()
                        self.ui.comboBox_4.setCurrentText(values.split('_')[1])
                if str(len(self.value_store)) == self.total_question:
                    self.ui.pushButton_5.show()
        except Exception as e:
            print(e)

    def add_model_selected_button(self):
        sub_option = ''
        if (self.current_image_index + 1) > 0:
            if self.sender().text() == 'ng':
                self.ui.comboBox_4.show()
                sub_option = '_'.join((self.sender().text(), self.ui.comboBox_4.currentText()))
            if self.sender().text() == "good":
                self.ui.comboBox_4.hide()
                self.ui.comboBox_4.close()
                sub_option = '_'.join((self.sender().text(), 'none'))
            self.value_store[self.current_image_index + 1] = sub_option
            self.update_add_model_color()

    def update_combo_selection(self, index):
        try:
            if (self.current_image_index + 1) > 0:
                option_text = self.ui.comboBox_4.currentText()
                if "ng" in self.value_store.get(self.current_image_index + 1, ""):
                    self.value_store[self.current_image_index + 1] = f"ng_{option_text}"
                self.update_add_model_color()
        except Exception as e:
            print(f"Error in update_combo_selection: {e}")

    def play_video(self):
        if self.video_capture and self.video_capture.isOpened():
            ret, frame = self.video_capture.read()
            if ret:
                rgb_image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                h, w, ch = rgb_image.shape
                bytes_per_line = ch * w
                qt_image = QImage(rgb_image.data, w, h, bytes_per_line, QImage.Format_RGB888)
                self.pixmap = QPixmap.fromImage(qt_image)
                self.ui.image_label_2.setPixmap(self.pixmap)
                self.ui.image_label_2.setScaledContents(True)
                QTimer.singleShot(33, self.play_video)  # approximately 30 FPS
            else:
                self.video_capture.release()

    def add_model_submit_button(self):
        try:
            model_name = self.ui.label_newmodelname.text().strip()
            if model_name:
                if model_name in os.listdir(file_dict):
                    QMessageBox.warning(self, 'Warning', 'Model Name already exist')
                else:
                    # video_base_path =
                    base_path = "Aoi_prj_file/" + model_name
                    dic = [f"{key}_{value}_{model_name}" for key, value in self.value_store.items()]
                    print(dic)
                    os.makedirs(base_path, exist_ok=True)
                    if len(dic) >= len(self.img_loc):
                        for index, image_path in enumerate(self.img_loc):
                            _, extension = os.path.splitext(image_path)
                            image_name = os.path.basename(dic[index] + extension)
                            new_image_path = os.path.join(base_path, image_name)
                            if extension == '.mp4':
                                shutil.copy2(image_path, base_path)
                                os.rename(os.path.join(base_path, os.path.basename(image_path)), new_image_path)
                            else:
                                image = cv2.imread(image_path)
                                cv2.imwrite(new_image_path, image)
                        QMessageBox.information(self, 'Success', 'Model and images have been successfully saved.')
                        self.main_window.show()
                        self.close()
                    else:
                        QMessageBox.warning(self, 'Warning', 'Please select the value.')
            else:
                QMessageBox.warning(self, 'Warning', 'Please enter the model name.')
        except Exception as e:
            print(e)



class EditModelWindow(QWidget):
    def __init__(self, main_window):
        super().__init__()
        self.setWindowTitle("Edit Model Window")
        self.main_window = main_window
        self.layout = QVBoxLayout()

        back_button = QPushButton("Back")
        self.layout.addWidget(back_button)
        back_button.clicked.connect(self.go_back)

        self.edit_model_label = QLabel("Model Name :")
        self.layout.addWidget(self.edit_model_label)

        self.lineEdit = QLineEdit()
        self.layout.addWidget(self.lineEdit)
        self.lineEdit.textChanged.connect(self.edit_model_filter_combobox)

        self.edit_model_option_box = QComboBox()
        self.folder = os.listdir(file_dict)
        for file in self.folder:
            self.edit_model_option_box.addItem(file)
        self.layout.addWidget(self.edit_model_option_box)

        self.search_model_submit_button = QPushButton("Submit")
        self.layout.addWidget(self.search_model_submit_button)
        self.search_model_submit_button.clicked.connect(self.display_edit_model)

        self.left_side_button = QPushButton("<")
        self.left_side_button.clicked.connect(self.edit_model_on_left_button_clicked)

        self.right_side_button = QPushButton(">")
        self.right_side_button.clicked.connect(self.edit_model_on_right_button_clicked)

        self.edit_model_good_button = QPushButton("good")

        self.edit_model_ng_button = QPushButton("ng")

        self.submit_edit_model_button = QPushButton("Submit")
        self.submit_edit_model_button.clicked.connect(self.submit_edit_model)

        self.image_label = QLabel()
        self.setLayout(self.layout)
        self.edit_model_current_image_index = 0
        self.value_store = {}
        self.img_loc = ''

    def go_back(self):
        self.main_window.show()
        self.close()

    def edit_model_filter_combobox(self, text):
        try:
            self.edit_model_option_box.clear()
            edit_model_filtered_items = [item for item in self.folder if text.lower() in item.lower()]
            self.edit_model_option_box.addItems(edit_model_filtered_items)
        except Exception as e:
            print(e)

    def edit_model_on_left_button_clicked(self):
        try:
            if self.edit_model_current_image_index > 0:
                self.edit_model_current_image_index -= 1
                self.display_edit_model()
        except Exception as e:
            print(e)

    def edit_model_on_right_button_clicked(self):
        try:
            option = file_dict + self.edit_model_option_box.currentText()
            images = [filename for filename in os.listdir(option) if
                      filename.endswith(('.jpg', '.jpeg', '.png', '.gif', '.bmp'))]
            if self.edit_model_current_image_index < len(images) - 1:
                self.edit_model_current_image_index += 1
                self.display_edit_model()
        except Exception as e:
            print(e)

    def display_edit_model(self):
        try:
            option = file_dict + self.edit_model_option_box.currentText()
            images = [filename for filename in os.listdir(option) if
                      filename.endswith(('.jpg', '.jpeg', '.png', '.gif', '.bmp'))]
            if images:
                image_path = os.path.join(option, images[self.edit_model_current_image_index])
                self.img_loc = [os.path.join(option, img) for img in images]
                pixmap = QPixmap(image_path)
                self.image_label.setPixmap(pixmap)
                self.layout.addWidget(self.image_label)
                self.layout.addWidget(self.edit_model_good_button)
                self.layout.addWidget(self.edit_model_ng_button)
                self.layout.addWidget(self.left_side_button)
                self.layout.addWidget(self.right_side_button)
                self.layout.addWidget(self.submit_edit_model_button)
                self.edit_model_good_button.setStyleSheet("background-color: None;")
                self.edit_model_ng_button.setStyleSheet("background-color: None;")
                self.update_edit_model_color()
                self.edit_model_good_button.clicked.connect(self.edit_model_selected_button)
                self.edit_model_ng_button.clicked.connect(self.edit_model_selected_button)
        except Exception as e:
            print(e)

    def update_edit_model_color(self):
        try:
            if self.value_store:
                for key, values in self.value_store.items():
                    if values == 'good' and (self.edit_model_current_image_index + 1) == key:
                        self.edit_model_good_button.setStyleSheet("background-color: #00FF00;")
                        self.edit_model_ng_button.setStyleSheet("background-color: None;")
                    if values == 'ng' and (self.edit_model_current_image_index + 1) == key:
                        self.edit_model_ng_button.setStyleSheet("background-color: #00FF00;")
                        self.edit_model_good_button.setStyleSheet("background-color: None;")
        except Exception as e:
            print(e)

    def edit_model_selected_button(self):
        try:
            if (self.edit_model_current_image_index + 1) > 0:
                self.value_store[self.edit_model_current_image_index + 1] = self.sender().text()
                self.update_edit_model_color()
        except Exception as e:
            print(e)

    def submit_edit_model(self):
        try:
            model_name = os.path.dirname(self.img_loc[0]).split('/')[1]
            if self.value_store.items():
                for sno, img_path in enumerate(self.value_store.items()):
                    if str(img_path[0]) == str(os.path.basename(self.img_loc[sno]).split('_')[0]):
                        _, extension = os.path.splitext(self.img_loc[sno])
                        img_loc = '_'.join((str(img_path[0]), str(img_path[1]), model_name))
                        full_img_loc = ''.join((img_loc, extension))
                        os.rename(self.img_loc[sno], '/'.join((os.path.dirname(self.img_loc[sno]), full_img_loc)))
                        QMessageBox.information(self, 'Success', 'Model and images have been successfully saved.')
                        self.main_window.show()
                        self.close()
            else:
                QMessageBox.warning(self, 'Warning', 'Please select the value.')
        except Exception as e:
            print(e)


if __name__ == "__main__":
    import sys
    from PySide2.QtWidgets import QApplication

    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
