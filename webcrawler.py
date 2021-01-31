import folder
import web


def main():
    url_goc = input('Nhập link khởi đầu: ')
    so_luong_trang = int(input('nhập số lượng trang: '))
    url_goc = web.sua_url_goc(url_goc)
    waiting_line = web.tim_url(url_goc, url_goc)
    history = web.tim_va_duyet_hang_cho(waiting_line, url_goc, so_luong_trang)
    folder.tao_thu_muc(input('Nhập tên thư mục lưu file: '))
    folder.luu_tat_ca_file(history, so_luong_trang)

if __name__ == '__main__':
    main()

