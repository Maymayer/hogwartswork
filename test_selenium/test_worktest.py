import pytest


def test_read_todic():
    with open('memberinfo.txt', encoding='UTF-8') as file_object:
        lines = file_object.readlines()
    members = []
    keys = lines[0].split('\t')
    row = 1
    row_max = len(lines)
    print(row_max)
    while row != row_max:
        member_row = lines[row].split('\t')
        i = 0
        member = {}
        for key in keys:
            member.update({key: member_row[i]})
            i += 1
        print(member)
        members.append(member)
        row += 1
    print(members)
