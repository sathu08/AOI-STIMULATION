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


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.next_window = None
        self.login_window = None
        self.ui = Ui_MainWindow()
        # self.ui.setupUi(self)
        self.setWindowTitle("Main Window")
        self.layout = QVBoxLayout()  # Define layout as an instance variable
        # Option Box
        # self.option_box = QComboBox()
        # self.option_box.addItem("Take Test")
        # self.option_box.addItem("Login Page")
        # self.option_box.currentIndexChanged.connect(self.option_changed)
        # self.layout.addWidget(self.option_box)
        self.login_button_request = QPushButton('Login Page')
        self.login_button_request.clicked.connect(self.login_option_changed)
        self.layout.addWidget(self.login_button_request)
        self.take_test_button_request = QPushButton('Take Test')
        self.take_test_button_request.clicked.connect(self.take_test_option_changed)
        self.layout.addWidget(self.take_test_button_request)
        # Search Box
        self.lineEdit = QLineEdit()
        self.layout.addWidget(self.lineEdit)
        self.lineEdit.textChanged.connect(self.filter_combobox)
        # Test Option Box
        self.test_option_box = QComboBox()
        folder = os.listdir(file_dict)
        for file in folder:
            self.test_option_box.addItem(file)
        self.layout.addWidget(self.test_option_box)
        self.test_option_box.show()
        # Input Field
        self.input_field = LabeledLineEdit("Employee ID:")
        self.layout.addWidget(self.input_field)
        self.input_field.show()
        # Login Page User Name Fields
        self.login_username_input_field = LabeledLineEdit("Username:")
        self.layout.addWidget(self.login_username_input_field)
        self.login_username_input_field.hide()
        # Login Page Password Fields
        self.login_password_input_field = LabeledLineEdit("Password:")
        self.login_password_input_field.line_edit.setEchoMode(QLineEdit.Password)
        self.layout.addWidget(self.login_password_input_field)
        self.login_password_input_field.hide()
        # Login Button
        self.login_button = QPushButton("Login")
        self.login_button.clicked.connect(self.login)
        self.layout.addWidget(self.login_button)
        self.login_button.hide()
        # Submit Button
        self.submit_button = QPushButton("Submit")
        self.submit_button.clicked.connect(self.submit)
        self.layout.addWidget(self.submit_button)
        self.submit_button.show()

        self.setLayout(self.layout)

    def login_option_changed(self):
        # Login Page
        self.lineEdit.hide()
        self.test_option_box.hide()
        self.input_field.hide()
        self.login_username_input_field.show()
        self.login_password_input_field.show()
        self.submit_button.hide()
        self.login_button.show()

    def take_test_option_changed(self):
        # Take Test
        self.test_option_box.show()
        self.lineEdit.show()
        self.input_field.show()
        self.login_username_input_field.hide()
        self.login_password_input_field.hide()
        self.submit_button.show()
        self.login_button.hide()

    def filter_combobox(self, text):
        try:
            self.test_option_box.clear()
            folder = os.listdir(file_dict)
            filtered_items = [item for item in folder if text.lower() in item.lower()]
            self.test_option_box.addItems(filtered_items)
        except Exception as e:
            print(e)

    def login(self):
        try:
            username = self.login_username_input_field.text()
            password = self.login_password_input_field.text()
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
            option = self.test_option_box.currentText()
            user_input = self.input_field.text().strip()
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
                print(selected_option)
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


class ExamWindow(QWidget):
    def __init__(self, option, user_input, option_selected, personal_details, main_window):
        super().__init__()
        self.video_capture = None
        self.setWindowTitle("Next Window")
        self.main_window = main_window
        self.layout = QVBoxLayout()  # Create a layout instance variable

        self.details = (option, user_input, option_selected, personal_details)
        self.option_label = QLabel("Option: " + option)
        self.layout.addWidget(self.option_label)

        self.input_label = QLabel("Employee ID: " + user_input)
        self.layout.addWidget(self.input_label)

        for detail in personal_details:
            self.name_label = QLabel("Employee Name: " + detail[1])
            self.dep_label = QLabel("Employee Department: " + detail[2])
        self.layout.addWidget(self.name_label)
        self.layout.addWidget(self.dep_label)

        self.video_image_label = QLabel()  # Removed reference to self.central_widget
        self.layout.addWidget(self.video_image_label)
        self.sno_label = QLabel('')
        self.layout.addWidget(self.sno_label)

        self.button_layout = QHBoxLayout()
        self.good_button = QPushButton("good")
        self.ng_button = QPushButton("ng")

        self.sub_option_comboBox = QComboBox()
        if option.split('_')[0] == 'AOI':
            for option in AOI_option_file_dict:
                self.sub_option_comboBox.addItem(option.strip())
        if option.split('_')[0] == 'EOL':
            for option in EOL_option_file_dict:
                self.sub_option_comboBox.addItem(option.strip())
        self.sub_option_comboBox.currentIndexChanged.connect(self.update_combo_selection)

        self.answer_store = {}
        self.test_option_buttons = []
        for option_text in option_selected:
            test_option_button = QPushButton(option_text.split('_')[0])
            test_option_button.setToolTip(option_text)  # Set full detail as tooltip
            self.test_option_buttons.append(test_option_button)  # Add button to the list
            self.layout.addWidget(test_option_button)
        # Connect the clicked signal of each button to the selected_option method
        for button in self.test_option_buttons:
            button.clicked.connect(self.selected_option)
        self.Submit_button = QPushButton("Submit")
        self.Submit_button.clicked.connect(self.test_submit)
        self.model_current_image_index = 0
        self.setLayout(self.layout)

    def display_model(self):
        try:
            option = file_dict + self.details[0]
            self.sno_label.setText(str(self.model_current_image_index + 1))
            images = [filename for filename in os.listdir(option) if
                      filename.endswith(('.jpg', '.jpeg', '.png', '.gif', '.bmp'))]
            video = [filename for filename in os.listdir(option) if
                     filename.endswith('.mp4')]
            if images:
                image_path = os.path.join(option, images[self.model_current_image_index])
                self.img_loc = [os.path.join(option, img) for img in images]
                pixmap = QPixmap(image_path)
                self.video_image_label.setPixmap(pixmap)

            if video:
                ret, frame = self.video_capture.read()
                if ret:
                    rgb_image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                    h, w, ch = rgb_image.shape
                    bytes_per_line = ch * w
                    qt_image = QImage(rgb_image.data, w, h, bytes_per_line, QImage.Format_RGB888)
                    pixmap = QPixmap.fromImage(qt_image)
                    self.video_image_label.setPixmap(pixmap)
                    self.video_image_label.setScaledContents(True)
            self.button_layout.addWidget(self.good_button)
            self.button_layout.addWidget(self.ng_button)
            self.layout.addLayout(self.button_layout)
        except Exception as e:
            print(e)

    def selected_option(self):
        try:
            self.clicked_button = self.sender()
            self.sno_label.setText(self.clicked_button.text())
            if self.clicked_button:
                full_option_text = self.clicked_button.toolTip()
                path_end_file = full_option_text.endswith('.mp4')
                self.good_button.setStyleSheet("background-color: None;")
                self.ng_button.setStyleSheet("background-color: None;")
                self.button_layout.addWidget(self.good_button)
                self.button_layout.addWidget(self.ng_button)
                self.layout.addLayout(self.button_layout)
                self.layout.addWidget(self.sub_option_comboBox)
                self.sub_option_comboBox.hide()
                self.good_button.clicked.connect(self.answer_clicked)
                self.ng_button.clicked.connect(self.answer_clicked)
                self.update_color()
                self.layout.addWidget(self.Submit_button)
                if path_end_file:
                    video_path = file_dict + "/" + self.details[0] + "/" + full_option_text
                    self.video_capture = cv2.VideoCapture(video_path)
                    self.play_video()
                else:
                    image_path = file_dict + "/" + self.details[0] + "/" + full_option_text
                    self.pixmap = QPixmap(image_path)
                    if not self.pixmap.isNull():
                        self.video_image_label.setPixmap(self.pixmap)
                        self.video_image_label.setFixedSize(self.pixmap.size())
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
                self.video_image_label.setPixmap(self.pixmap)
                self.video_image_label.setScaledContents(True)
                QTimer.singleShot(33, self.play_video)  # approximately 30 FPS
            else:
                self.video_capture.release()

    def update_color(self):
        try:
            if self.answer_store:
                for key, values in self.answer_store.items():
                    if values.split('_')[0] == 'good' and self.clicked_button.text() == key:
                        self.good_button.setStyleSheet("background-color: #00FF00;")
                        self.ng_button.setStyleSheet("background-color: None;")
                        self.sub_option_comboBox.hide()
                    if values.split('_')[0] == 'ng' and self.clicked_button.text() == key:
                        self.ng_button.setStyleSheet("background-color: #00FF00;")
                        self.good_button.setStyleSheet("background-color: None;")
                        self.sub_option_comboBox.show()
                        self.sub_option_comboBox.setCurrentText(values.split('_')[1])
        except Exception as e:
            print(e)

    def answer_clicked(self):
        try:
            if self.clicked_button:
                if self.sender().text() == "good":
                    self.sub_option_comboBox.hide()
                    self.sub_option_comboBox.close()
                    self.clicked_button.setStyleSheet("background-color: #00FF00;")
                    sub_option = '_'.join((self.sender().text(), 'none'))

                if self.sender().text() == "ng":
                    self.sub_option_comboBox.show()
                    self.clicked_button.setStyleSheet("background-color: #00FF00;")
                    sub_option = '_'.join((self.sender().text(), self.sub_option_comboBox.currentText()))
                self.answer_store[self.clicked_button.text()] = sub_option
                self.update_color()
        except Exception as e:
            print(e)

    def update_combo_selection(self, index):
        try:
            if self.clicked_button:
                option_text = self.sub_option_comboBox.currentText()
                if "ng" in self.answer_store.get(self.clicked_button.text(), ""):
                    self.answer_store[self.clicked_button.text()] = f"ng_{option_text}"
                self.update_color()
        except Exception as e:
            print(f"Error in update_combo_selection: {e}")


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
                            if img.split('_')[0] == i and img.split('_')[1] == j.split('_')[0] and img.split('_')[2] == j.split('_')[1]:
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


class ScoreWindow(QWidget):
    def __init__(self, score, user_details, main_window, incorrect_question, incorrect_answer):
        super().__init__()
        self.setWindowTitle("Score Window")
        self.main_window = main_window
        self.layout = QVBoxLayout()

        self.detail = [detail for _ in user_details[3] for detail in _]
        self.correct_answers, self.total_questions = score[0], score[1]
        self.Pass_Percentage = int((self.correct_answers / self.total_questions) * 100)
        self.status = ("pass" if self.Pass_Percentage >= 50 else 'fail')

        self.username_label = QLabel("User Name: " + self.detail[1])
        self.layout.addWidget(self.username_label)

        self.employee_id_label = QLabel("Employee ID: " + self.detail[0])
        self.layout.addWidget(self.employee_id_label)

        self.department_label = QLabel("Department: " + self.detail[2])
        self.layout.addWidget(self.department_label)

        self.incorrect_question = json.dumps(incorrect_question)
        self.incorrect_answer = json.dumps(incorrect_answer)
        self.user_details = user_details

        self.score_label = QLabel("Score: " + str(self.correct_answers))
        self.layout.addWidget(self.score_label)

        self.total_questions_label = QLabel("Total Questions: " + str(self.total_questions))
        self.layout.addWidget(self.total_questions_label)

        self.percentage_label = QLabel("Percentage: " + str(self.Pass_Percentage) + "%")
        self.layout.addWidget(self.percentage_label)

        self.status_label = QLabel("Percentage: " + str(self.status))
        self.layout.addWidget(self.status_label)

        self.insert_data_base()
        self.write_report()

        back_button = QPushButton("Back")
        self.layout.addWidget(back_button)
        back_button.clicked.connect(self.go_back)
        self.setLayout(self.layout)

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
            pdf.add_page()
            if self.report_details:
                incorrect_questions = json.loads(self.report_details[9])
                incorrect_answers = json.loads(self.report_details[8])
                image_paths = image
                table_data_insert = tuple(zip(incorrect_questions, incorrect_answers, image_paths,
                                              [os.path.basename(path).split('_')[1].split('.')[0] for path in
                                               image_paths]))
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
                        if os.path.basename(item).split('.')[1] == 'mp4':
                            image_path = 'icons/video_img.png'
                            image = cv2.imread(image_path)
                            cv2.putText(image, item, (0, 774), cv2.FONT_HERSHEY_SIMPLEX,
                                        6, (255, 0, 0), 25, cv2.LINE_AA)
                            output_path = 'icons/convert_video_img.png'
                            cv2.imwrite(output_path, image)
                            pdf.image(output_path, x=x + 5, y=y + 5, w=cell_width - 10, h=cell_height - 10)
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


class AdminWindow(QWidget):
    def __init__(self, option, user_input, main_window):
        super().__init__()
        self.add_model_window = None
        self.report_window = None
        self.edit_model_window = None
        self.create_account_window = None
        self.setWindowTitle("Admin Window")
        self.main_window = main_window
        self.layout = QVBoxLayout()

        self.option_label = QLabel("Option: " + option)
        self.layout.addWidget(self.option_label)

        back_button = QPushButton("Back")
        self.layout.addWidget(back_button)
        back_button.clicked.connect(self.go_back)

        create_button = QPushButton("Create Account")
        self.layout.addWidget(create_button)
        create_button.clicked.connect(self.create_account)

        add_model_button = QPushButton("Add Model")
        self.layout.addWidget(add_model_button)
        add_model_button.clicked.connect(self.add_model)

        edit_model_button = QPushButton("Edit Model")
        self.layout.addWidget(edit_model_button)
        edit_model_button.clicked.connect(self.edit_model)

        view_report_button = QPushButton("Report")
        self.layout.addWidget(view_report_button)
        view_report_button.clicked.connect(self.view_report)

        self.setLayout(self.layout)

    def go_back(self):
        self.main_window.show()
        self.close()

    def create_account(self):
        self.create_account_window = CreateAccountWindow(self)
        self.create_account_window.show()
        self.hide()

    def add_model(self):
        self.add_model_window = AddModelWindow(self)
        self.add_model_window.show()
        self.hide()

    def edit_model(self):
        self.edit_model_window = EditModelWindow(self)
        self.edit_model_window.show()
        self.hide()

    def view_report(self):
        self.report_window = ViewReportWindow(self)
        self.report_window.show()
        self.hide()


class ViewReportWindow(QWidget):
    def __init__(self, main_window):
        super().__init__()
        self.setWindowTitle("Report Window")
        self.main_window = main_window
        self.layout = QVBoxLayout()

        back_button = QPushButton("Back")
        self.layout.addWidget(back_button)
        back_button.clicked.connect(self.go_back)

        self.report_search = LabeledLineEdit("Search :")
        self.layout.addWidget(self.report_search)

        self.report_submit_button = QPushButton("Submit")
        self.layout.addWidget(self.report_submit_button)
        self.report_submit_button.clicked.connect(self.report_button)

        self.open_report_button = QPushButton("Open")
        self.graphical_report_button = QPushButton("Graphical Report")
        self.report_file = []
        self.report_file_option_box = QComboBox()

        self.setLayout(self.layout)

    def go_back(self):
        self.main_window.show()
        self.close()

    def report_button(self):
        try:
            report_search = self.report_search.text()
            report_folder = os.listdir(report_file_dict)
            report_fetch_details = [report for report in report_folder if report_search in report]
            if report_fetch_details:
                for file in report_fetch_details:  # Changed report_folder to report_fetch_details
                    path = ' '.join((file.split('_')[0], (
                        '-'.join((file.split('_')[1][:4], file.split('_')[1][4:6], file.split('_')[1][6:])))))
                    self.report_file_option_box.addItem(path)
                    self.report_file_option_box.setToolTip(file)
                self.layout.addWidget(self.report_file_option_box)
                self.layout.addWidget(self.open_report_button)
                self.open_report_button.clicked.connect(self.open_pdf)
                self.layout.addWidget(self.graphical_report_button)
                self.graphical_report_button.clicked.connect(self.graphical_report_)
            else:
                QMessageBox.warning(self, "Warning", "Please enter correct Employee ID")
        except Exception as e:
            print(e)

    def graphical_report_(self):
        try:
            report_search = self.report_search.text()
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
                        canvas = self.plot(employee_details)
                        self.layout.addWidget(canvas)
                else:
                    QMessageBox.warning(self, "Warning", "Please enter correct Employee ID")
        except Exception as e:
            print(e)

    def open_pdf(self):
        try:
            option = self.report_file_option_box.toolTip()
            print(option)
            os.startfile(os.path.join(report_file_dict, option))
            self.report_file_option_box.clear()
        except Exception as e:
            print(e)

    def plot(self, data):
        figure, ax = plt.subplots()
        dates = [entry[0] for entry in data]
        models = [entry[1] for entry in data]
        scores = [int(entry[2]) for entry in data]
        ax.bar(dates, scores)  # Changed self.canvas.ax to ax

        for i, score in enumerate(scores):
            value = ','.join((str(models[i]), str(score)))
            ax.text(i, score + 0.4, value, ha='center')
        ax.set_xlabel('Date')
        ax.set_ylabel('Score')
        ax.set_title('Scores by Date and Model')
        figure.tight_layout()
        canvas = FigureCanvas(figure)  # Changed self.canvas to FigureCanvas(figure)
        return canvas


class CreateAccountWindow(QWidget):
    def __init__(self, main_window):
        super().__init__()
        self.setWindowTitle("Create Account Window")
        self.main_window = main_window
        self.layout = QVBoxLayout()

        back_button = QPushButton("Back")
        self.layout.addWidget(back_button)
        back_button.clicked.connect(self.go_back)

        self.create_user_name = LabeledLineEdit("Username:")
        self.layout.addWidget(self.create_user_name)

        self.create_employee_id = LabeledLineEdit("Employee ID:")
        self.layout.addWidget(self.create_employee_id)

        self.create_department = LabeledLineEdit("Department:")
        self.layout.addWidget(self.create_department)

        self.create_account_submit_button = QPushButton("Submit")
        self.layout.addWidget(self.create_account_submit_button)
        self.create_account_submit_button.clicked.connect(self.create_account_submit)
        self.setLayout(self.layout)

    def create_account_submit(self):
        try:
            details = self.create_user_name.text(), self.create_employee_id.text(), self.create_department.text()
            if self.create_user_name.text() and self.create_employee_id.text() and self.create_department.text():
                conn = sqlite3.connect(database)
                cur = conn.cursor()
                check_detail = cur.execute('select Emp_id from personal_details where Emp_id= ?',
                                           (details[1],)).fetchone()
                if not check_detail:
                    cur.execute('insert into personal_details ( Name,Emp_id, Dep) values (?,?,?)', details)
                    conn.commit()
                    conn.close()
                    QMessageBox.information(self, 'Account Created Successfully', 'Account created successfully!')
                    self.create_user_name.line_edit.clear()
                    self.create_employee_id.line_edit.clear()
                    self.create_department.line_edit.clear()
                else:
                    QMessageBox.warning(self, 'Warning', 'Employee details already exists')
            else:
                QMessageBox.warning(self, 'Warning', 'Please enter correct Username and Department')
        except Exception as e:
            print(e)

    def go_back(self):
        self.main_window.show()
        self.close()


class AddModelWindow(QWidget):
    def __init__(self, main_window):
        super().__init__()
        self.video_capture = None
        self.setWindowTitle("Add Model Window")
        self.main_window = main_window
        self.layout = QVBoxLayout()
        back_button = QPushButton("Back")
        self.layout.addWidget(back_button)
        back_button.clicked.connect(self.go_back)

        self.folder_label = QLabel("No folder selected")
        self.layout.addWidget(self.folder_label)
        self.model_name_label = QLineEdit(self)
        self.layout.addWidget(self.model_name_label)
        self.model_name_label.setPlaceholderText("Type something here...")

        self.select_folder_button = QPushButton("Select Folder ")
        self.select_folder_button.clicked.connect(self.select_folder)
        self.select_folder_button.hide()
        self.layout.addWidget(self.select_folder_button)


        self.video_image_label = QLabel()  # Added image_label

        self.model_name_label.textChanged.connect(self.check_input)
        self.left_side_button = QPushButton("<", self)
        self.left_side_button.clicked.connect(self.on_left_button_clicked)

        self.right_side_button = QPushButton(">", self)
        self.right_side_button.clicked.connect(self.on_right_button_clicked)

        self.sub_option_comboBox = QComboBox()
        self.add_model_good_button = QPushButton("good")
        self.add_model_ng_button = QPushButton("ng")
        self.submit_add_model_button = QPushButton("Submit")
        self.setLayout(self.layout)
        self.value_store = {}
        self.current_image_index = 0
        self.img_loc = ''

    def check_input(self):
        if self.model_name_label.text().split('_')[0] == 'AOI':
            self.select_folder_button.show()
            for option in AOI_option_file_dict:
                self.sub_option_comboBox.addItem(option.strip())
        elif self.model_name_label.text().split('_')[0] == 'EOL':
            self.select_folder_button.show()
            for option in EOL_option_file_dict:
                self.sub_option_comboBox.addItem(option.strip())
        else:
            self.select_folder_button.hide()

    def select_folder(self):
        try:
            global folder_path
            options = QFileDialog.Options()
            folder_path = QFileDialog.getExistingDirectory(self, "Select Folder", options=options)

            self.sub_option_comboBox.currentIndexChanged.connect(self.update_combo_selection)
            if folder_path:
                self.folder_label.setText(folder_path)
                self.display_image()
                self.submit_add_model_button.clicked.connect(self.add_model_submit_button)
        except Exception as e:
            print(e)

    def on_left_button_clicked(self):
        try:
            if self.current_image_index > 0:
                self.current_image_index -= 1
                self.display_image()
        except Exception as e:
            print(e)

    def on_right_button_clicked(self):
        try:
            global folder_path
            folder_path = self.folder_label.text()
            images = [filename for filename in os.listdir(folder_path) if
                      filename.endswith(('.jpg', '.jpeg', '.png', '.gif', '.bmp', '.mp4'))]
            if self.current_image_index < len(images) - 1:
                self.current_image_index += 1
                self.display_image()
        except Exception as e:
            print(e)

    def display_image(self):
        try:
            global folder_path
            folder_path = self.folder_label.text()
            images = [filename for filename in os.listdir(folder_path) if
                      filename.endswith(('.jpg', '.jpeg', '.png', '.gif', '.bmp', '.mp4'))]
            if images and self.model_name_label.text():
                image_path = os.path.join(folder_path, images[self.current_image_index])
                self.img_loc = [os.path.join(folder_path, img) for img in images]
                if image_path.endswith('.mp4'):
                    self.video_capture = cv2.VideoCapture(image_path)
                    self.play_video()
                else:
                    self.pixmap = QPixmap(image_path)
                    self.video_image_label.setPixmap(self.pixmap)
                    self.video_image_label.setFixedSize(self.pixmap.size())
                    self.layout.addWidget(self.video_image_label)
                self.layout.addWidget(self.add_model_good_button)
                self.layout.addWidget(self.add_model_ng_button)
                self.layout.addWidget(self.left_side_button)
                self.layout.addWidget(self.right_side_button)
                self.add_model_good_button.setStyleSheet("background-color: None;")
                self.add_model_ng_button.setStyleSheet("background-color: None;")
                self.layout.addWidget(self.sub_option_comboBox)
                self.layout.addWidget(self.submit_add_model_button)
                self.sub_option_comboBox.hide()
                self.update_add_model_color()
                self.add_model_good_button.clicked.connect(self.add_model_selected_button)
                self.add_model_ng_button.clicked.connect(self.add_model_selected_button)
        except Exception as e:
            print(e)

    def update_add_model_color(self):
        try:
            if self.value_store:
                for key, values in self.value_store.items():
                    if values.split('_')[0] == 'good' and (self.current_image_index + 1) == key:
                        self.add_model_good_button.setStyleSheet("background-color: #00FF00;")
                        self.add_model_ng_button.setStyleSheet("background-color: None;")
                        self.sub_option_comboBox.hide()
                    if values.split('_')[0] == 'ng' and (self.current_image_index + 1) == key:
                        self.add_model_ng_button.setStyleSheet("background-color: #00FF00;")
                        self.add_model_good_button.setStyleSheet("background-color: None;")
                        self.sub_option_comboBox.show()
                        self.sub_option_comboBox.setCurrentText(values.split('_')[1])
        except Exception as e:
            print(e)

    def add_model_selected_button(self):
        sub_option = ''
        if (self.current_image_index + 1) > 0:
            if self.sender().text() == 'ng':
                self.sub_option_comboBox.show()
                sub_option = '_'.join((self.sender().text(), self.sub_option_comboBox.currentText()))
            if self.sender().text() == "good":
                self.sub_option_comboBox.hide()
                self.sub_option_comboBox.close()
                sub_option = '_'.join((self.sender().text(), 'none'))
            self.value_store[self.current_image_index + 1] = sub_option
            self.update_add_model_color()

    def update_combo_selection(self, index):
        try:
            if (self.current_image_index + 1) > 0:
                option_text = self.sub_option_comboBox.currentText()
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
                self.video_image_label.setPixmap(self.pixmap)
                self.video_image_label.setScaledContents(True)
                QTimer.singleShot(33, self.play_video)  # approximately 30 FPS
            else:
                self.video_capture.release()

    def add_model_submit_button(self):
        try:
            model_name = self.model_name_label.text().strip()
            if model_name:
                if model_name in os.listdir(file_dict):
                    QMessageBox.warning(self, 'Warning', 'Model Name already exist')
                else:
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

    def go_back(self):
        self.main_window.show()
        self.close()


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
