#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 15 20:21:47 2023

@author: boon
"""

from airflow import DAG
from airflow.operators.python import PythonOperator, BranchPythonOperator
from airflow.operators.bash import BashOperator

from random import randint
from datetime import datetime



def _choose_best_model(ti):
    accuracies = ti.xcom_pull(task_ids=[
        'training_model_A',
        'training_model_B',
        'training_model_C'
        ])
    best_accuracy = max(accuracies)
    if (best_accuracy > 8):
        return 'accurate' #task id
    return 'inaccurate' #other task id


def _training_model():
    return randint(1, 10)



# with datetime(2023,1,1) and @daily, it will be triggered 01/02/2023 at 00:00
with DAG("my_dag", start_date=datetime(2023, 1, 1), 
         schedule_interval="@daily", catchup=False) as dag:
    
    #task1
    training_model_A = PythonOperator(
        task_id="training_model_A",
        python_callable=_training_model
        )
    
    #task2
    training_model_B = PythonOperator(
        task_id="training_model_B",
        python_callable=_training_model
        )
    
    #task3
    training_model_C = PythonOperator(
        task_id="training_model_C",
        python_callable=_training_model
        )
    
    #task4
    choose_best_model = BranchPythonOperator(
        task_id="choose_best_model",
        python_callable=_choose_best_model
        )
    
    #branch task
    accurate = BashOperator(
        task_id="accurate",
        bash_command="echo 'accurate'"
        )
    #branch task
    inaccurate = BashOperator(
        task_id="inaccurate",
        bash_command="echo 'inaccurate'"
        )
    
    ## set dependencies, can use lists for simultaneous tasks 
    #and >> or << for downstream/upstream
    [training_model_A, training_model_B, training_model_C] >> choose_best_model >> [accurate, inaccurate]
