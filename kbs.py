import streamlit as st
import data
from defineFunction import goiy_thucdon, luong_calo, tinh_bmi, tinh_bmr, trang_thai_co_the


def suggest():
    chi_so_bmr = tinh_bmr(chieucao, cannang, dotuoi, gioitinh)
    suggestion_progress.progress(20)

    chi_so_bmi = tinh_bmi(chieucao, cannang)
    suggestion_progress.progress(40)
    st.write(f'Chỉ số BMI là: {round(chi_so_bmi, 2)}')

    trangthai_cothe = trang_thai_co_the(chi_so_bmi)
    suggestion_progress.progress(60)
    st.write(f'Trạng thái cơ thể là: {trangthai_cothe}')

    tp_nendung, tp_konendung = goiy_thucdon(options)
    suggestion_progress.progress(80)
    if(options):
        st.write(f'Bạn đang mắc bệnh {", ".join(list(options))}')

    luong_calo_canthiet = luong_calo(chi_so_bmr, chi_so_bmi, mucdohoatdong)

    suggestion_progress.progress(90)
    if(tp_nendung):
        st.write(f'Nên bổ sung: {", ".join(list(tp_nendung))}')

    suggestion_progress.progress(95)
    if(tp_konendung):
        st.write(f'Nên hạn chế: {", ".join(list(tp_konendung))}')

    suggestion_progress.progress(100)
    st.write(f'Lượng calo/ngày khuyến cáo: {round(luong_calo_canthiet)}')


st.title('Thực đơn cho người cao tuổi sau ốm')
disable = False
col1, col2 = st.columns(2)
with col1:
    gioitinh = st.selectbox('Giới tính', data.GIOITINH, disabled=disable)
    chieucao = st.number_input('Chiều cao', 1.0, 1.8, 1.5, disabled=disable)
    mucdohoatdong = st.selectbox('Mức độ hoạt động', data.MUCDOHOATDONG)
with col2:
    dotuoi = st.number_input('Tuổi', 60, 100, disabled=disable)
    cannang = st.number_input('Cân nặng', 30.0, 100.0, 70.0, disabled=disable)

options = st.multiselect('Các bệnh mắc phải', data.BENH, disabled=disable)
start = st.button('Bắt đầu')

if (start):
    disable = True
    suggestion_progress = st.progress(0)
    suggest()
    disable = False
