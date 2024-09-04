import os

import arrow
from dotenv import load_dotenv
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
from kurly import clusters

# 환경 변수에서 Slack 토큰, 채널을 로드
load_dotenv()
SLACK_TOKEN = os.environ.get("SLACK_TOKEN")
def send_slack_message(message, channel):
    try:
        client = WebClient(token=SLACK_TOKEN)
        client.chat_postMessage(channel=channel, text=message)
    except SlackApiError as e:
        print(f"Error sending message to {channel} : {e}")
def main():
    for cluster in clusters:
        # 메시지 제목 설정
        header = f":loudspeaker: *『인사총무팀 공지』* <!channel>\n\n"

        notice_msg = (
            f"안녕하세요? 평택 클러스터 구성원 여러분\n*평택 클러스터 출/퇴근 셔틀 이용 관련 안내사항 Remind* 공유 드립니다.\n"
            f"*（전체공지_매주1회）*\n\n"
            f"\n"
            f"\n"
            f":체크1: *자세한 자료는 스레드 참고 바랍니다!*\n\n"
            f"\n"
            f"\n"
            f"*첨부:one: - 셔틀 노선도*\n"
            f"*첨부:two: - 셔틀 노선 및 경유지 상세 이미지 포함*\n"
            f"*첨부:three: - 셔틀 승,하차 장소*\n"
            f"*첨부:four: - 셔틀 어플 사용 안내*\n"
            f"*첨부:five: - 셔틀 （퇴근）출발 시간 안내*\n\n"
            f"\n"
            f"\n"
            f"*자세한 자료는 스레드 참고 바랍니다!*\n\n"
            f"*문의사항 : 인사총무팀 총무/시설 담당자*\n\n"
            f"감사합니다.\n"
        )
 
        # 메시지 본문
        body = header + notice_msg

        # 슬랙 채널에 전송
        send_slack_message(body, cluster.channel)

if __name__ == "__main__":
    main()
