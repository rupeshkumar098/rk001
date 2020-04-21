

class course:
    c_id=''
    c_name=''
    c_duration=''

    def set_c(self, id, name, duration):
        self.c_id = id
        self.c_name = name
        self.c_duration = duration

    def show(self):
        print("Course Id = ", self.c_id)
        print("Course Name = ", self.c_name)
        print("Course Duration = ", self.c_duration)




class Employee:
    emp_id = ''
    name = ''
    age = ''


class Trainee(Employee):
    t_id = ''
    t_score = ''
    t_dict = {"Course Name": "Status"}

    def set_e(self,e_id,name,age):
        self.emp_id=e_id
        self.name=name
        self.age=age



    c_obj = course()


    def add_course_on_trainee_obj(self,id,name,duration):

        self.c_obj.c_id=id
        self.c_obj.c_name=name
        self.c_obj.c_duration=duration

    def update_course_on_trainee_obj(self,id,name,duration):
        self.c_obj.c_id = id
        self.c_obj.c_name = name
        self.c_obj.c_duration = duration





def main():
    #first_task
    t_obj=Trainee()
    t_obj.set_e('1283','Rupesh','21');


    #second Task
    c_obj1 = course();
    c_obj2 = course();
    c_obj3 = course();
    c_obj4 = course();
    c_obj5 = course();
    c_obj6 = course();

    c_obj1.set_c('01', 'AWS', '3 Month')
    c_obj2.set_c('02', 'Python', '6 Months')
    c_obj3.set_c('03', 'Node js', '2 Months')
    c_obj4.set_c('04', 'JAVA', '6 Months')
    c_obj5.set_c('05', 'Web Development', '3 Months')
    c_obj6.set_c('06', 'DBMS', '1 Months')

    #Third Task

    t_obj.add_course_on_trainee_obj('01','AWS','3 Months')
    #before updattion
    print("Before Updation")
    t_obj.c_obj.show()


    #fourth task
    t_obj.update_course_on_trainee_obj('02','Python','6 Months')
    #after updation
    print("\n","After Updation")
    t_obj.c_obj.show()




if __name__=="__main__":
    main()


