FROM python:3


WORKDIR /root/ResponseToFile

RUN git clone https://github.com/baiyanquan/ResponseToFile.git /root/ResponseToFile \
    && pip install --upgrade pip \
    && pip install requests -i https://pypi.tuna.tsinghua.edu.cn/simple\
    && pip install flask -i https://pypi.tuna.tsinghua.edu.cn/simple\
    && pip install flask_cors -i https://pypi.tuna.tsinghua.edu.cn/simple\
    && ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime\
    && echo 'Asia/Shanghai' >/etc/timezone

CMD ["python", "/root/ResponseToFile/app.py"]