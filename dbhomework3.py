import pymysql.cursors
import os


def connect_db(_password, _port):
    config = {
        'host': '127.0.0.1',
        'user': 'root',
        'password': _password,
        'port': int(_port),
        'db': 'python_ai',
        'charset': 'utf8',
        'cursorclass': pymysql.cursors.DictCursor,
    }
    return pymysql.connect(**config)


def select_member(_db, _cursor, _table):
    sql = f"SELECT * FROM {_table}"
    try:
        _cursor.execute(sql)
        _db.commit()
    except:
        _db.rollback()


def select_where_data(_db, _cursor, _table, _member_id):
    sql = f"SELECT * FROM {_table} WHERE member_id = {_member_id}"
    try:
        _cursor.execute(sql)
        _db.commit()
    except:
        _db.rollback()


def select_tel(_db, _cursor, _table):
    sql = f"SELECT * FROM {_table} INNER JOIN tel ON member.id = tel.member_id"
    try:
        _cursor.execute(sql)
        _db.commit()
    except:
        _db.rollback()


def insert_member(_db, _cursor, _table, _name, _birthday, _address):
    sql = f"INSERT INTO {_table}(\
       id, name, birthday, address) \
       VALUES (NULL, '%s', '%s', '%s' )" % \
          (_name, _birthday, _address)
    try:
        _cursor.execute(sql)
        _db.commit()
    except:
        _db.rollback()


def insert_tel(_db, _cursor, _table, _member_id, _tel):
    sql = f"INSERT INTO {_table}(\
       id, member_id, tel) \
       VALUES (NULL, '%s', '%s' )" % \
          (_member_id, _tel)
    try:
        _cursor.execute(sql)
        _db.commit()
    except:
        _db.rollback()


def update_member(_db, _cursor, _table, _id, _name, _birthday, _address):
    sql = f"UPDATE {_table} SET name = '%s', birthday = '%s', address = '%s' \
                              WHERE id = '%s'" % (_name, _birthday, _address, _id)
    try:
        _cursor.execute(sql)
        _db.commit()
    except:
        _db.rollback()


def delete_data(_db, _cursor, _table, _id):
    sql = f"DELETE FROM {_table} WHERE id = '%s'" % (_id)
    try:
        _cursor.execute(sql)
        _db.commit()
    except:
        _db.rollback()


def print_all_data(_result):
    for row in _result:
        print(row)


def input_command():
    print("(0) 離開程式")
    print("(1) 顯示會員列表")
    print("(2) 新增會員資料")
    print("(3) 更新會員資料")
    print("(4) 刪除會員資料")
    print("(5) 新增會員的電話")
    print("(6) 刪除會員的電話")
    return input("指令：")


def append_tel(_members, _tels):
    for member in _members:
        member_id = member["id"]
        tel_list = []
        for tel in _tels:
            tel_id = tel["member_id"]
            if member_id == tel_id:
                tel_list.append(tel["tel"])
        member["tel_list"] = tel_list


def check_command(_command):
    table_member = "member"
    table_tel = "tel"
    os.system("cls")

    if _command == "0":
        db.close()

    if _command == "1":
        select_member(db, cursor, table_member)
        members = cursor.fetchall()
        select_tel(db, cursor, table_member)
        tels = cursor.fetchall()
        append_tel(members, tels)
        print_all_data(members)
        check_command(input_command())

    if _command == "2":
        name = input("請輸入會員姓名：")
        birthday = input("請輸入會員生日：")
        address = input("請輸入會員地址：")
        insert_member(db, cursor, table_member, name, birthday, address)
        check_command(input_command())

    if _command == "3":
        select_member(db, cursor, table_member)
        members = cursor.fetchall()
        select_tel(db, cursor, table_member)
        tels = cursor.fetchall()
        append_tel(members, tels)
        print_all_data(members)
        input_id = input("請選擇你要修改的資料編號：")
        name = input("請輸入會員姓名：")
        birthday = input("請輸入會員生日：")
        address = input("請輸入會員地址：")
        update_member(db, cursor, table_member, input_id, name, birthday, address)
        check_command(input_command())

    if _command == "4":
        select_member(db, cursor, table_member)
        members = cursor.fetchall()
        select_tel(db, cursor, table_member)
        tels = cursor.fetchall()
        append_tel(members, tels)
        print_all_data(members)
        input_id = input("請選擇你要刪除的資料編號：")
        delete_data(db, cursor, table_member, input_id)
        check_command(input_command())

    if _command == "5":
        select_member(db, cursor, table_member)
        members = cursor.fetchall()
        select_tel(db, cursor, table_member)
        tels = cursor.fetchall()
        append_tel(members, tels)
        print_all_data(members)
        input_id = input("請選擇要添加電話的會員編號：")
        input_tel = input("請輸入電話：")
        insert_tel(db, cursor, table_tel, input_id, input_tel)
        check_command(input_command())

    if _command == "6":
        select_member(db, cursor, table_member)
        members = cursor.fetchall()
        select_tel(db, cursor, table_member)
        tels = cursor.fetchall()
        append_tel(members, tels)
        print_all_data(members)
        input_id = input("請選擇要刪除電話的會員編號：")
        select_where_data(db, cursor, table_tel, input_id)
        print_all_data(cursor.fetchall())
        input_id = input("請輸入要刪除的電話編號：")
        delete_data(db, cursor, table_tel, input_id)
        check_command(input_command())


password = input("請輸入資料庫root密碼：")
port = input("請輸入資料庫的Port：")

db = connect_db(password, port)
cursor = db.cursor()

check_command(input_command())
