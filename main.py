import csv

class TestReport:
    """
        Класс для представления отчета о тестировании.

        Атрибуты:
        test_id (int): уникальный идентификатор теста
        test_name (str): название теста
        date_executed (str): дата выполнения теста
        time_executed (str): время выполнения теста
        result (str): результат теста
        """
    def __init__(self, test_id, test_name, date_executed, time_executed, result):
        """
                Конструктор класса TestReport.

                Args:
                test_id (int): уникальный идентификатор теста
                test_name (str): название теста
                date_executed (str): дата выполнения теста
                time_executed (str): время выполнения теста
                result (str): результат теста
                """
        self.test_id = test_id
        self.test_name = test_name
        self.date_executed = date_executed
        self.time_executed = time_executed
        self.result = result

    def __str__(self):
        """
               Метод для форматированного вывода информации об отчете о тестировании.

               Returns:
               str: строка, содержащая информацию об отчете о тестировании
               """
        return f'Test ID: {self.test_id}\nTest Name: {self.test_name}\nDate Executed: {self.date_executed}\nTime Executed: {self.time_executed}\nResult: {self.result}\n'

    def __eq__(self, other):
        """
               Метод для проверки эквивалентности двух отчетов о тестировании.

               Args:
               other (TestReport): другой отчет о тестировании

               Returns:
               bool: True, если отчеты эквивалентны, False в противном случае
               """
        return (self.test_id == other.test_id
                and self.test_name == other.test_name
                and self.date_executed == other.date_executed
                and self.time_executed == other.time_executed
                and self.result == other.result)

    def clone(self):
        """
                Метод для создания копии отчета о тестировании.

                Returns:
                TestReport: копия отчета о тестировании
                """
        return TestReport(self.test_id, self.test_name, self.date_executed, self.time_executed, self.result)

    @staticmethod
    def from_csv_row(row):
        """
                Статический метод для создания экземпляра класса TestReport из строки CSV.

                Args:
                row (list): список значений строки CSV

                Returns:
                TestReport: экземпляр класса TestReport, созданный из строки CSV
                """
        return TestReport(int(row[0]), row[1], row[2], row[3], row[4])

    def to_csv_row(self):
        """
        Метод to_csv_row(self) возвращает список строк, представляющих текущий экземпляр класса TestReport,
         которые можно записать в CSV файл. Этот метод используется для записи экземпляров класса TestReport в CSV файл.
        """
        return [str(self.test_id), self.test_name, self.date_executed, self.time_executed, self.result]


# чтение файла в массив объектов
test_reports = []
with open('lab_0_read.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for row in reader:
        test_reports.append(TestReport.from_csv_row(row))

# вывод на экран
for report in test_reports:
    print(report)