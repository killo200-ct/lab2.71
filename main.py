import csv

class TestReport:
    def __init__(self, test_id, test_name, date_executed, time_executed, result):
        self.test_id = test_id
        self.test_name = test_name
        self.date_executed = date_executed
        self.time_executed = time_executed
        self.result = result

    def __str__(self):
        return f'Test ID: {self.test_id}\nTest Name: {self.test_name}\nDate Executed: {self.date_executed}\nTime Executed: {self.time_executed}\nResult: {self.result}\n'

    def __eq__(self, other):
        return (self.test_id == other.test_id
                and self.test_name == other.test_name
                and self.date_executed == other.date_executed
                and self.time_executed == other.time_executed
                and self.result == other.result)

    def clone(self):
        return TestReport(self.test_id, self.test_name, self.date_executed, self.time_executed, self.result)

    @staticmethod
    def from_csv_row(row):
        return TestReport(int(row[0]), row[1], row[2], row[3], row[4])

    def to_csv_row(self):
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