import asyncio
import os
import time
from datetime import datetime
import psycopg2
from dotenv import load_dotenv

load_dotenv()
with psycopg2.connect(database=os.getenv('database'),
                      user=os.getenv('user'),
                      password=os.getenv('password'),
                      host=os.getenv('host'),
                      port=os.getenv('port')) as conn:
    with conn.cursor() as cur:
        def create_table():
            time.sleep(1)
            create_table_qurry="""
            create table cars(
            id serial           primary key ,
            car_name            varchar(100) not null ,
            car_number          varchar(200) not null ,
            car_color           varchar(200) default 'red',
            car_price           decimal not null 
            )"""
            cur.execute(create_table_qurry)
            conn.commit()
            print("table yaratildi")

        def insert_table():
            time.sleep(2)
            insert_into_table_query="""
            insert into cars(car_name,car_number,car_price)
            values ('matiz','40AG518k',4000),
                   ('spark','10DF564A',8000),
                   ('gentra','01ZZ777Z',14000),
                   ('malibu','10TT333T',35000);"""
            cur.execute(insert_into_table_query)
            conn.commit()
            print("malumot qo'shildo")

        def select_table():
            time.sleep(4)
            select_table_query="""
            select * from cars;"""
            cur.execute(select_table_query)
            conn.commit()
            print(cur.fetchall())

        def alter_table():
            time.sleep(3)
            alter_table_query="""
            alter table cars
            add column car_year int ;"""
            cur.execute(alter_table_query)
            conn.commit()
            print("colmn qo'shildi")

        def update_table():
            time.sleep(5)
            update_table_query="""
            update cars set car_color='qizl' where id=2;"""
            cur.execute(update_table_query)
            conn.commit()
            print("malumot o;zgartirldi")

        def search_table():
            time.sleep(5)
            search_cars_query="""
            select car_name,car_number from cars where like car_name='matiz';"""
            cur.execute(search_cars_query)
            conn.commit()
            print("ialash yakunlandi")

        def delete_table():
            time.sleep(6)
            delete_table_query="""
            delete from cars where id=1;"""
            cur.execute(delete_table_query)
            conn.commit()
            print('malimot ochirildi')

        if __name__=="__main__":
            print(datetime.now())
            create_table()
            insert_table()
            select_table()
            alter_table()
            update_table()
            select_table()
            delete_table()
            print(datetime.now())
