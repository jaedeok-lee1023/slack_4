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
    "2025-09-29",  # 입사자 없음
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
        header = f":loudspeaker: *『인사총무팀 공지』* <!channel>\n\n"

        notice_msg = (
            f"안녕하세요? 평택 클러스터 구성원 여러분\n*평택 클러스터 출/퇴근 셔틀 이용 관련 안내사항 Remind* 공유 드립니다.\n"
            f"*（전체공지_매주1회）*\n\n"
            f"\n"
            f":체크1: *셔틀 관련 채널은 <#C05PK6K7XRN|14_셔틀버스_평택> 이용 바랍니다.*\n\n"
            f"\n"
            f"*첨부:one: - <https://50072f98-e1d6-4b35-b1e5-5564ad1fcebf.usrfiles.com/ugd/50072f_b8214cc01dfe4ff7ba4ed238e3f89b59.xlsx|셔틀 노선도>*\n"
            f"*첨부:two: - <https://50072f98-e1d6-4b35-b1e5-5564ad1fcebf.usrfiles.com/ugd/50072f_0f2444ef6472420eb0fc32758ee7f3b8.pptx|셔틀 노선 및 경유지 상세 이미지 포함>*\n"
            f"*첨부:three: - <https://50072f98-e1d6-4b35-b1e5-5564ad1fcebf.usrfiles.com/ugd/50072f_4138997ae0db4d3fa5789cab2c718ded.pdf|셔틀 승,하차 장소>*\n"
            f"*첨부:four: - <https://50072f98-e1d6-4b35-b1e5-5564ad1fcebf.usrfiles.com/ugd/50072f_b72245b692984e838e89f72711e2aea8.pdf|셔틀 어플 사용 안내>*\n"
            f"*첨부:five: - <https://static.wixstatic.com/media/50072f_db56f7e4de6a4f3a9941f4b2b0d55c6a~mv2.png|셔틀（퇴근）출발 시간 안내>*\n\n"
            f"\n"
            f"*자세한 자료는 :point_up: :point_up: 클릭하여 확인 부탁드립니다!*\n\n"
            f"*문의사항 : 인사총무팀 총무/시설 담당자*\n\n"
            f"감사합니다.\n"
        )
 
        # 메시지 본문
        body = header + notice_msg

        # 슬랙 채널에 전송
        send_slack_message(body, cluster.channel)

if __name__ == "__main__":
    main()
