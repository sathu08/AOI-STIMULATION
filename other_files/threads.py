import json
import sys, time
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence,
                           QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *
from PySide2.QtCore import *
import csv
import time
import os
import pika

from time import sleep                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             


class MySignal(QObject):

    sig = Signal(str)
    startpb = Signal()
    okinp = Signal(str,str)
    nginp = Signal(str,str)
    cttime = Signal(str)
    conn = Signal(bool)

class Mylongthread(QThread):

    def __init__(self, parent=None):
        QThread.__init__(self, parent)

        self.signal = MySignal()
        self.print = False
        self.qty = 0
        self.allprint = False
        self.data = ""
        
    def run(self):
        try:
            connection = None

            while connection is None:
                print("Establishing connection...")
                time.sleep(5)
                connection = self.establish_connection()
            # Start consuming messages
            print("connection established")            
            self.consume_messages(connection)
            self.signal.conn.emit(True)
            

            # Keep the main thread alive
            while True:
                time.sleep(1)

        except Exception as e:
            print(f"An unexpected error occurred: {e}")

        finally:
            if connection and connection.is_open:
                connection.close()
                
    def establish_connection(self):
        
        credentials = pika.PlainCredentials(username='cim', password='cim')
        connection_params = pika.ConnectionParameters(
            host='10.218.199.159',
            port=5672,
            credentials=credentials)
        try:
            return pika.BlockingConnection(connection_params)
        except pika.exceptions.AMQPConnectionError as e:
            print(f"Error connecting to RabbitMQ: {e}")
            return None
        
    def consume_messages(self,connection):
        channel = connection.channel()

        exchange_name = 'panasonic.broker.materialverify'
        queue_name = 'jay'
       # queue_name = 'mes.pmi.panasonic.materialverify'

        # Declare the exchange with the correct durable setting
        channel.exchange_declare(
            exchange=exchange_name,
            exchange_type='fanout',
            durable=True,
            auto_delete=True
        )

        # Declare the queue as durable
        channel.queue_declare(queue=queue_name, durable=True)

        # Bind the queue to the exchange
       # channel.queue_bind(exchange=exchange_name, queue=queue_name)

        def callback(ch, method, properties, body):
           # print(f"Received message: {body} with headersfvkvgvk: {properties.headers}")
           data = (properties.headers)
            #data = '''+ (properties.headers) +'''
            
           #  data = f" '''{properties.headers}'''"
           # # print(data,type(data))
            
           self.signal.sig.emit(str(data))
           self.data = data
            
            

        channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)

        print("Waiting for messages. To exit press CTRL+C")
        channel.start_consuming()
        








class MyInputs(QThread):

    def __init__(self, parent=None):
            QThread.__init__(self, parent)
            self.inp = Ui_MainWindow()

            self.signal = MySignal()
            self.inpstart = True
            self.partstatus = False
            self.okinp = False
            self.nginp = False
            self.manual = False

    def run(self):
        
        self.ctst = time.time()

        
        print("started")

        while True:

            while self.inpstart == True:
                print("in start loop")

                if switch1.is_pressed:
                    print("switch pressed")
                    self.signal.startpb.emit()
                    self.ctst = time.time()
                    self.inpstart = False

                time.sleep(0.2)



               

            while self.partstatus == True:
                print(self.partstatus)
                print("am in second loop")
                if switch2.is_pressed:
                    done = time.time()
                    elapsed = (done - self.ctst)
                    ct = (str(elapsed))
                    ctn = ct[0:5]
                    self.signal.okinp.emit("Pass",ctn)
                    print("ok pressed")
                    self.partstatus = False
                    #self.inpstart = True
                    print("ok pressed")



                if switch4.is_pressed:
                    done = time.time()
                    elapsed = (done - self.ctst)
                    ct = (str(elapsed))
                    ctn = ct[0:5]
                    self.signal.okinp.emit("Fail", ctn)
                    print("ng pressed")
                    self.partstatus = False
                    #self.inpstart = True
                    print("ng pressed")
                    
                time.sleep(0.2)

            while self.manual == True:

                print("inmanual loop")
                self.signal.manin.emit("0")

                if switch1.is_pressed:
                    self.signal.manin.emit("1")
                    print("1 pressed")
                if switch2.is_pressed:
                    self.signal.manin.emit("2")
                if switch4.is_pressed:
                    self.signal.manin.emit("3")
                  

                time.sleep(0.2)


            time.sleep(0.2)

        


           










