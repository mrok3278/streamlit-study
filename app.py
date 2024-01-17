import streamlit as st
import os
import base64
import random
import time
import datetime
import pandas as pd
    
from streamlit_option_menu import option_menu
# from streamlit_modal import Modal

from gtts import gTTS

home_path = ''
level_list = []
character_list = []

def init():
    global home_path
    global character_list
    global level_list
    
    home_path = os.path.dirname(os.path.abspath(__file__)).replace('\\', '/')
    
    level_list = ['8급', '7급']
    
    character_list = [
        {'level': 8, 'char': '九', 'mean': '아홉', 'pron': '구'},
        {'level': 8, 'char': '金', 'mean': '금속', 'pron': '금'},
        {'level': 8, 'char': '南', 'mean': '남쪽', 'pron': '남'},
        {'level': 8, 'char': '男', 'mean': '남자', 'pron': '남'},
        {'level': 8, 'char': '女', 'mean': '여자', 'pron': '녀'},
        {'level': 8, 'char': '東', 'mean': '동쪽', 'pron': '동'},
        {'level': 8, 'char': '六', 'mean': '여섯', 'pron': '륙'},
        {'level': 8, 'char': '母', 'mean': '어머니', 'pron': '모'},
        {'level': 8, 'char': '木', 'mean': '나무', 'pron': '목'},
        {'level': 8, 'char': '門', 'mean': '문', 'pron': '문'},
        {'level': 8, 'char': '父', 'mean': '아버지', 'pron': '부'},
        {'level': 8, 'char': '北', 'mean': '북쪽', 'pron': '북'},
        {'level': 8, 'char': '四', 'mean': '넉', 'pron': '사'},
        {'level': 8, 'char': '三', 'mean': '석', 'pron': '삼'},
        {'level': 8, 'char': '西', 'mean': '서쪽', 'pron': '서'},
        {'level': 8, 'char': '水', 'mean': '물', 'pron': '수'},
        {'level': 8, 'char': '十', 'mean': '열', 'pron': '십'},
        {'level': 8, 'char': '五', 'mean': '다섯', 'pron': '오'},
        {'level': 8, 'char': '月', 'mean': '달', 'pron': '월'},
        {'level': 8, 'char': '二', 'mean': '두', 'pron': '이'},
        {'level': 8, 'char': '人', 'mean': '사람', 'pron': '인'},
        {'level': 8, 'char': '日', 'mean': '날', 'pron': '일'},
        {'level': 8, 'char': '一', 'mean': '하나', 'pron': '일'},
        {'level': 8, 'char': '子', 'mean': '아들', 'pron': '자'},
        {'level': 8, 'char': '弟', 'mean': '남동생', 'pron': '제'},
        {'level': 8, 'char': '七', 'mean': '일곱', 'pron': '칠'},
        {'level': 8, 'char': '土', 'mean': '흙', 'pron': '토'},
        {'level': 8, 'char': '八', 'mean': '여덟', 'pron': '팔'},
        {'level': 8, 'char': '兄', 'mean': '형', 'pron': '형'},
        {'level': 8, 'char': '火', 'mean': '불', 'pron': '화'},
        {'level': 7, 'char': '江', 'mean': '강(하천)', 'pron': '강'},
        {'level': 7, 'char': '口', 'mean': '입', 'pron': '구'},
        {'level': 7, 'char': '內', 'mean': '안', 'pron': '내'},
        {'level': 7, 'char': '年', 'mean': '해(년)', 'pron': '년'},
        {'level': 7, 'char': '大', 'mean': '큰', 'pron': '대'},
        {'level': 7, 'char': '目', 'mean': '눈', 'pron': '목'},
        {'level': 7, 'char': '白', 'mean': '흰', 'pron': '백'},
        {'level': 7, 'char': '山', 'mean': '산', 'pron': '산'},
        {'level': 7, 'char': '上', 'mean': '위', 'pron': '상'},
        {'level': 7, 'char': '小', 'mean': '작을', 'pron': '소'},
        {'level': 7, 'char': '手', 'mean': '손', 'pron': '수'},
        {'level': 7, 'char': '外', 'mean': '바깥', 'pron': '외'},
        {'level': 7, 'char': '右', 'mean': '오른', 'pron': '우'},
        {'level': 7, 'char': '入', 'mean': '들', 'pron': '입'},
        {'level': 7, 'char': '足', 'mean': '발', 'pron': '족'},
        {'level': 7, 'char': '左', 'mean': '왼', 'pron': '좌'},
        {'level': 7, 'char': '中', 'mean': '가운데', 'pron': '중'},
        {'level': 7, 'char': '靑', 'mean': '푸른', 'pron': '청'},
        {'level': 7, 'char': '出', 'mean': '날', 'pron': '출'},
        {'level': 7, 'char': '下', 'mean': '아래', 'pron': '하'}
    ]


def main():
    with st.sidebar:
        choice = option_menu(
            'Menu',
            ['한자 학습', '오답노트', '모의 시험'],
            icons=['book-half', 'arrow-through-heart', 'pencil'],
            styles={
                'container': {'padding': '4!important', 'background-color': '#08c7b4'},
                'icon': {'color': 'black', 'font-size': '25px'},
                'nav-link': {'font-size': '16px', 'text-align': 'left', 'margin': '0px', '--hover-color': '#9be0d9'},
                'nav-link-selected': {'background-color': '#07B3A2'},
            },
            menu_icon='app-indicator',
            default_index=0,
        )

    if choice == '한자 학습':
        show_study()
    elif choice == '모의 시험':
        show_exam()
    elif choice == '오답노트':
        show_wrong_note()


def show_study():
    global level_list
    
    st.header(':open_book: 한자 학습')

    level_choice = st.selectbox('', level_list)

    show_study_character(int(level_choice[0]))


def show_study_character(level):
    global home_path
    global character_list

    # 해당 급수의 한자 리스트에서 25개의 문제 선택
    study_list = [item for item in character_list if item['level'] == level]

    # 문제 순차적으로 표시
    tile_col1 = None
    tile_col2 = None
    for i, item in enumerate(study_list):
        if tile_col1 is None or i % 2 == 0:
            tile_col1, tile_col2 = st.columns(2)

        tile_col = (tile_col1 if i % 2 == 1 else tile_col2)

        tile = tile_col.container(height=150)
        tile.header(f"{item['char']} {item['mean']} {item['pron']}")
        
        # 버튼 컬럼
        btn_col1, btn_col2, btn_col3 = tile.columns((4,4,4))
        
        # 듣기 버튼
        btn_listen = btn_col1.button(':loudspeaker: 듣기 ', f'l_{level}_{i}')
        if btn_listen:
            file_path = f"{home_path}/{level}_{item['mean']} {item['pron']}.mp3"
            
            if os.path.isfile(file_path) == False:
                audio_file = gTTS(text=f"{item['mean']} {item['pron']}", lang='ko')
                audio_file.save(file_path)
                
            if os.path.isfile(file_path):
                play_audio(file_path)

        # 쓰기 버튼
        btn_write = btn_col2.button(':writing_hand: 쓰기 ', f'w_{level}_{i}')
        if btn_write:
            show_study_modal(item)

def show_study_modal(item):
    # modal_write = Modal(title="쓰기", key="write")
    
    # cols = st.columns(8)
    # with cols[7]:
    #     with modal_write.container():
    #         btn_check = st.button(':white_check_mark: 확인 ', 'check')
    #         if btn_check:
    #             modal_write.close()
                
    #         btn_close = st.button(':x: 닫기 ', 'close')
    #         if btn_close:
    #             modal_write.close()
    pass


def show_exam():
    global character_list
    
    st.header(':pencil: 모의 시험')
    
    col_1, col_2 = st.columns((4, 8))
    level_choice = col_1.selectbox('', level_list)
    
    btn_exam = st.button(':white_check_mark: 시작 ', 'check')
    
    timer_col1, timer_col2, timer_col3 = st.columns((4, 4, 4))
    
    exam_tile = st.container(height=300)
    
    if btn_exam:
        quest_list, exam_list = build_exam_list(int(level_choice[0]))
        show_exam_item(exam_tile, quest_list, exam_list)
        
        show_timer(timer_col1, timer_col2, timer_col3)

def build_exam_list(level):
    global character_list
    
    quest_list = random.sample([item for item in character_list if item['level'] >= level], 25)
    exam_list = []
    
    for i, quest_item in enumerate(quest_list):
        sample_list = [item for item in character_list if item['char'] != quest_item['char']]
        sample_list = random.sample(sample_list, 3)
        sample_list.append(quest_item)
        
        random.shuffle(sample_list)
        
        for sample_item in sample_list:
            new_item = sample_item.copy()
            new_item['no'] = i
            exam_list.append(new_item)
            
    return quest_list, exam_list


def show_exam_item(exam_tile, quest_list, exam_list):
    for step in range(0, 1):
        quest_item = quest_list[step]

        with exam_tile:
            exam_cont = st.empty()
            exam_cont.markdown(f"<h1 style='text-align: center;'>{quest_item['char']}</h1>", unsafe_allow_html=True)
            list = [item for item in exam_list if item['no'] == step]
            df = pd.DataFrame([{'번호': i+1, '뜻': f"{item['mean']} {item['pron']}"} for i, item in enumerate(list)])
            exam_table = st.table(df.set_index('번호'))
            
def show_timer(timer_col1, timer_col2, timer_col3):
    now = datetime.datetime.now()
    end_time = now + datetime.timedelta(minutes=40)
    
    with timer_col1:
        tile = st.container(height=100)
        tile.metric('시작 시간', now.strftime('%H:%M:%S'))

    with timer_col2:
        tile = st.container(height=100)
        tile.metric('종료 시간', end_time.strftime('%H:%M:%S'))
        
    with timer_col3:
        tile = st.container(height=100)
        
        with tile:
            ph = st.empty()
            while datetime.datetime.now() < end_time:
                diff = max((end_time - datetime.datetime.now()).seconds, 0)
                ph.metric('남은 시간', f'{diff // 60:02d}:{diff % 60:02d}')
                if(diff == 0): break
                
                time.sleep(1)
                
                
def show_wrong_note():
    st.header(':heartbeat: 오답노트')
    # 오답노트 관련 내용 표시

def play_audio(file_path):
    with open(file_path, "rb") as audio_file:
        audio_bytes = audio_file.read()
        audio_base64 = base64.b64encode(audio_bytes).decode()
        audio_tag = f"<audio type='audio/mp3' autoplay='true' src='data:audio/mp3;base64,{audio_base64}'>"
        st.markdown(audio_tag, unsafe_allow_html=True)
        
if __name__ == '__main__':
    init()
    main()
