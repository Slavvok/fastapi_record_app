import os

from models import Record

file_path = os.getcwd()

FILE = "file.csv"
FILE_PATH = os.path.join(file_path, FILE)


def save_record(data: str) -> Record:
    new_id = 1
    with open(FILE_PATH, "r+") as file:
        lines = file.readlines()

        if lines:
            last_id = int(lines[-1].split(",")[0])
            new_id = last_id + 1

    # with open(FILE_PATH, "a") as file:
        # csv_writer = csv.writer(file, delimiter=',')
        file.write(",".join([str(new_id), data]) + "\n")
        record = Record(id=new_id, data=data)

    return record


def fetch_record(number: int) -> Record | None:
    with open(FILE_PATH, "r") as file:
        lines = file.readlines()
        for line in lines[1:]:
            line = line.replace("\n", "").split(",")
            if line[0] == number:
                record = Record(id=line[0], data=line[1])
                return record
        return None


def fetch_record_list(first: int, last: int) -> list[Record]:
    with open(FILE_PATH, "r") as file:
        lines = file.readlines()
        records = []
        for line in lines[1:]:
            line = line.replace("\n", "").split(",")
            if first <= int(line[0]) <= last:
                record = Record(id=line[0], data=line[1])
                records.append(record)
        return records
