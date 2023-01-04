import data
import time


def tinh_bmr(chieucao, cannang, dotuoi, gioitinh):
    time.sleep(1)
    chieucao *= 100.0
    if gioitinh == 'Ông':
        return 66 + 13.7 * cannang + 5 * chieucao - 6.8 * dotuoi
    elif gioitinh == 'Bà':
        return 655 + 9.6 * cannang + 1.8 * chieucao - 4.7 * dotuoi


def luong_calo(bmr, bmi, mucdohd):
    time.sleep(1)
    bmr *= quy_doi_muc_do_hoat_dong(mucdohd)
    if(bmi < 20):
        return bmr * 1.20
    elif(bmi < 25):
        return bmr * 1.10
    elif(bmi <= 27):
        return bmr * 1
    elif(bmi <= 30):
        return bmr * 0.90
    else:
        return bmr * 0.80


def quy_doi_muc_do_hoat_dong(mucdo):
    return data.MUCDOHOATDONG.get(mucdo)


def trang_thai_co_the(bmi):
    time.sleep(1)
    if(bmi < 20):
        return 'Thiếu cân'
    elif(bmi < 25):
        return 'Dưới mức bình thường'
    elif(bmi <= 27):
        return 'Bình thường'
    elif(bmi <= 30):
        return 'Trên mức bình thường'
    else:
        return 'Thừa cân'


def tinh_bmi(chieucao, cannang):
    time.sleep(1)
    return cannang / (chieucao**2)


def goiy_thucdon(benhmacphai):
    time.sleep(2)
    nhom_tp_nen = set()
    for benh in benhmacphai:
        nhom_tp_nen.update(data.BENH[benh].get('nen'))

    nhom_tp_konen = set()
    for benh in benhmacphai:
        nhom_tp_konen.update(data.BENH[benh].get('konen'))

    for nhom_tp in nhom_tp_konen:
        nhom_tp_nen.discard(nhom_tp)

    tp_nen = set()
    tp_konen = set()

    for nhomtp in nhom_tp_konen:
        tp_konen.update(data.NHOM_THUC_PHAM.get(nhomtp, [nhomtp]))

    for nhomtp in nhom_tp_nen:
        tp_nen.update(data.NHOM_THUC_PHAM.get(nhomtp, [nhomtp]))

    for tp in tp_konen:
        tp_nen.discard(tp)

    return tp_nen, tp_konen
