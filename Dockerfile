# We're using Ubuntu 20.10
FROM ximfine/xproject:buster

#
# Clone repo and prepare working directory
#
RUN git clone -b main https://github.com/Patrick489/PatrickBot /root/userbot
RUN mkdir /root/userbot/.bin
WORKDIR /root/userbot

#Install python requirements
RUN pip3 install -r https://raw.githubusercontent.com/Patrick489/PatrickBot/main/requirements.txt

CMD ["python3","-m","userbot"]
