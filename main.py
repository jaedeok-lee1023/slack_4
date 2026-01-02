import os
import sys
import datetime
import arrow
from dotenv import load_dotenv
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
from kurly import clusters

# 🎯 한국 공휴일 목록 (YYYY-MM-DD 형식)
HOLIDAYS = {
    "2025-01-01",  # 신정
    "2025-03-01",  # 삼일절
    "2025-05-05",  # 어린이날
    "2025-05-06",  # 대체공휴일
    "2025-06-02",  # 대체공휴일
    "2025-06-03",  # 선거일
    "2025-06-06",  # 현충일
    "2025-08-15",  # 광복절
    "2025-10-03",  # 개천절
    "2025-10-06",  # 추석
    "2025-10-07",  # 추석연휴
    "2025-10-08",  # 대체공휴일
    "2025-10-09",  # 한글날
    "2025-12-25",  # 크리스마스
}

# 📆 오늘 날짜 가져오기
today = datetime.date.today().strftime("%Y-%m-%d")

# 🚫 오늘이 공휴일이면 실행하지 않고 종료
if today in HOLIDAYS:
    print(f"📢 오늘({today})은 공휴일이므로 실행하지 않습니다.")
    sys.exit(0)

# 환경 변수에서 Slack 토큰 로드
load_dotenv()
SLACK_TOKEN = os.environ.get("SLACK_TOKEN")

def send_slack_message(message, channel):
    try:
        client = WebClient(token=SLACK_TOKEN)
        client.chat_postMessage(channel=channel, text=message)
    except SlackApiError as e:
        print(f"⚠️ Error sending message to {channel} : {e}")

def main():
    for cluster in clusters:
        # 메시지 제목 설정
        header = f"*[공지｜클러스터 셔틀버스 안내]*\n\n\n"

        notice_msg = (
            f"1. *중요도* : 상\n"
            f"2. *대상* : 평택 클러스터 임직원 전체\n"
            f"3. *주요 내용*\n\n"
            f"\n"
            f"안녕하세요? 평택 클러스터 구성원 여러분!\n\n"
            f"출/퇴근 셔틀 관련 안내 드립니다.\n"
            f"\n"
            f"\n"
            f":체크1: *셔틀 관련 채널은 <#C05PK6K7XRN|14_셔틀버스_평택> 이용 바랍니다.*\n\n"
            f"\n"
            f"*<https://kurlyptrc.notion.site/199905920f5180aa9c7efbbc9fd76803|셔틀 노선도>*\n"
            f"*<https://kurlyptrc.notion.site/199905920f5180aa9c7efbbc9fd76803|셔틀 어플 사용 및 탑승 장소 안내>*\n\n"
            f"\n"
            f"\n"
            f"*:slack: 문의사항 : FC운영표준화_통합RP_채용2 담당자*\n\n"
            f"감사합니다.\n"
        )
 
        # 메시지 본문
        body = header + notice_msg

        # 슬랙 채널에 전송
        send_slack_message(body, cluster.channel)

if __name__ == "__main__":
    main()
