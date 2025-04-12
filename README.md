# LangGraph 챗봇 프로젝트

이 프로젝트는 LangGraph를 활용하여 챗봇을 개발하는 방법을 보여줍니다. 챗봇은 OpenAI의 GPT 모델을 사용하여 사용자와 상호작용하며, 도구를 통합하여 더 나은 응답을 제공할 수 있습니다. 또한, 인간의 개입을 통해 복잡한 질문에 대한 응답 품질을 향상시킬 수 있습니다.

## 목차
- [기능](#기능)
- [설치](#설치)
- [사용법](#사용법)
- [예제](#예제)
- [기여](#기여)
- [라이센스](#라이센스)

## 기능
- OpenAI GPT 모델을 사용한 자연어 처리
- Tavily 검색 도구를 통한 웹 검색 기능
- Kakao API를 활용한 장소 검색 기능
- 인간 개입(Human-in-the-loop) 기능
- 대화 상태 관리 및 메모리 기능

## 설치

프로젝트를 실행하기 위해 필요한 라이브러리를 설치합니다. 아래 명령어를 실행하세요:

```bash
pip install -U python-dotenv notebook langgraph langchain_openai tavily-python langchain_community
```

### 환경변수 설정

`.env` 파일을 생성하고 다음 내용을 추가합니다:

```bash
OPENAI_API_KEY=본인의_OpenAI_API키
OPENAI_MODEL=gpt-4o-mini
TAVILY_API_KEY=본인의_tavily_api_key
KAKAO_API_KEY=본인의_kakao_api_key
```

## 사용법

1. **환경 설정**: 필요한 라이브러리를 설치하고 환경변수를 설정합니다.
2. **코드 실행**: Jupyter Notebook에서 제공된 `.ipynb` 파일을 열고 코드를 실행합니다.
3. **챗봇과 상호작용**: 사용자 입력을 통해 챗봇과 대화하며, 도구를 사용하여 추가 정보를 검색하거나 인간의 개입을 요청할 수 있습니다.

## 예제

### LangGraph 챗봇 사용 예제

```python
user_input = "AI 에이전트 개발을 위한 LangGraph의 특징에 대해 설명해주세요."
state = {"messages": [HumanMessage(content=user_input)]}
response = graph.invoke(state, config)
print(response["messages"][-1].content)
```

### Kakao API를 활용한 장소 검색 예제

```python
user_input = "서울에서 애견동반 가능한 카페 알려줘"
state = {"messages": [HumanMessage(content=user_input)]}
response = graph.invoke(state)
print(response["messages"][-1].content)
```
