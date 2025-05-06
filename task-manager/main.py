# ----------------------------
# -- Task Management System --
# ----------------------------

"""
هذا التطبيق يقوم بإدارة المهام 
1- إضافة مهمة جديدة
2- عرض جميع المهام
3- حذف مهمة
4- حفظ المهمة في ملف
5- خروج من البرنامج
"""

my_task = [] # قائمة لتخزين المهام

def add_task(): # دالة لإضافة مهمة جديدة
    print("إضافة مهمة جديدة")
    task = input("أدخل المهمة: ").strip()
    my_task.append(task)
    print(f"تم إضافة المهمة: {task}")

def show_tasks(): # دالة لعرض المهام
    print("عرض جميع المهام")
    if not my_task:
        print("لا توجد مهام")
    else:
        print("المهام:")
        for i, task in enumerate(my_task, start=1):
            print(f"{i}- {task}")

def delete_task(): # دالة لحذف مهمة
    print("حذف مهمة")
    if not my_task:
        print("لا توجد مهام")
    else:
        show_tasks()
        task_indix = int(input("أدخل رقم المهمة التي تريد حذفها: "))
        if 0 < task_indix <= len(my_task):
            removed_task = my_task.pop(task_indix - 1)
            print(f"تم حذف المهمة: {removed_task}")
            with open(r"D://Learn/Python/Task.txt", "w", encoding="utf-8") as file:
                for task in my_task:
                    file.write(task + "\n")
        else:
            print("رقم المهمة غير صحيح")

def save_tasks(): # دالة لحفظ المهام في ملف
    print("حفظ المهام في الملف")
    if not my_task:
        print("لا توجد مهام")
    else:
        with open(r"D://Learn/Python/Task.txt", "w", encoding="utf-8") as file:
            for task in my_task:
                file.write(task + "\n")
                print(f"تم حفظ المهمة: {task} في الملف")

def main(): # الدالة الرئسية
    while True:
        print("تطبيق إدارة المهام")
        print("1- إضافة مهمة جديدة")
        print("2- عرض جميع المهام")
        print("3- حذف مهمة")
        print("4- حفظ المهمة في الملف")
        print("5- خروج من البرنامج")
        choice = input("إختار خيار: ").strip()
        if choice == "1":
            add_task()
        elif choice == "2":
            show_tasks()
        elif choice == "3":
            delete_task()
        elif choice == "4":
            save_tasks()
        elif choice == "5":
            print("تم الخروج من التطبيق")
            break
        else:
            print("خيار غير صحيح")

main() # استدعاء الدالة الرئيسية