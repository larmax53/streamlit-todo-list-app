#   todo_list.py

import streamlit as st
from task import Task

def add_task(task_name: str):
    task_list.append(Task(task_name))
#end def

def mark_done(task: Task):
    task.is_done = True
#end def

def mark_not_done(task: Task):
    task.is_done = False
#end def

def delete_task(idx: int):
    del task_list[idx]
#end def


if 'task_list' not in st.session_state:
    st.session_state.task_list = []
#end if
task_list = st.session_state.task_list

with st.sidebar:
    task = st.text_input('Enter a task')
    if st.button('Add task', type='primary'):
        add_task(task)
    #end if
#end with

total_tasks = len(task_list)
completed_tasks = sum(1 for task in task_list if task.is_done)
metric_display = f'{completed_tasks}/{total_tasks} done'
st.metric('Task completion', metric_display, delta=None)

st.header("Today's to-dos", divider='gray')
#st.info(f'task_list: {task_list}')
for idx, task in enumerate(task_list):
    task_col, delete_col = st.columns([0.8, 0.2])
    label = f'~~{task.name}~~' if task.is_done else task.name
    checked = task_col.checkbox(label, task.is_done, key=f'task_{idx}')
    if checked and not task.is_done:
        mark_done(task)
        st.rerun()
    elif not checked and task.is_done:
        mark_not_done(task)
        st.rerun()
    #end if
    if delete_col.button('Delete', key=f'delete_{idx}'):
        delete_task(idx)
        st.rerun()
    #end if
#next
