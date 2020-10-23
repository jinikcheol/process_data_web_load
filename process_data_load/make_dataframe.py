import pandas as pd
from process import process_operate

def make_df(char3):

    # 데이터프레임 샘플
    df_sample = pd.DataFrame(process_operate.process_start(char3))

    # HTML로 변환하기
    html = df_sample.to_html()

    return html