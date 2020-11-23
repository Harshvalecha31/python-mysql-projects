from pr1 import Operation

o1 = Operation()

query1 = '''
create table if not exists Employee(id int auto_increment primary key,
name varchar(25) not null,
designation varchar(15) default 'fresher'
)
'''
#o1.createtable(query1)

query2 = '''
insert into Employee(name,designation) values('Jake','Senior HR')
'''
#o1.insertone(query2)
        
query3 = '''
insert into Employee(name,designation) values (%s,%s)
'''
vals = [
('James','Manager'),
('Julia','full stack1'),
('Jack','System Engineer'),
('Ryan','Web Developer'),
('Groot','full stack2')
]
#o1.insertmany(query3,vals)

query4 = '''
select * from Employee where name = 'Jack'
'''
#o1.selectone(query4)

query5 = '''
select * from Employee
'''
#o1.selectall(query5)

query6 = '''
update Employee set name = 'zack' where name = 'Jack'
'''
#o1.update(query6)

query7 = '''
delete from Employee where designation = 'full stack1'
'''
#o1.deleterows(query7)

query8 = '''
drop table if exists Employee
'''
#o1.droptable(query8)

#o1.dropdatabase()