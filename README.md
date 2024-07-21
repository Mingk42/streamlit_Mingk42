# Hello, STREAMLIT
### 구성
실행할 수 있는 파일은 총 5개입니다.
- uber_pickups.py
- animation.py
- map.py
- plotting.py
- df.py

### 사용법
***
`streamlit run uber_pickups.py`을 입력하시면 uber delibery 정보를 아래와 같이 확인할 수 있습니다.
![image](https://github.com/user-attachments/assets/7f5eb2e1-eb74-4cdf-86c4-5276f228dca8)
***
`streamlit run animation.py`을 입력하시면 움직이는 이미지를 아래와 같이 확인할 수 있습니다.
![image](https://github.com/user-attachments/assets/07d7bdac-b42a-4179-b27c-ec460f0b18ec)
- 사이드바를 통해 동작의 세부사항을 변경할 수 있습니다.
> [!CAUTION]
> Separation > 1.48 일 때 오류를 발생시키며 조금씩 튀는 현상 발생
***
`streamlit run map.py`을 입력하시면 자전거 대여 정보를 아래와 같이 확인할 수 있습니다.
![image](https://github.com/user-attachments/assets/86373f09-fddf-488e-9f70-5c595aa03cd3)
***
`streamlit run plotting.py`을 입력하시면 난수로 생성되는 그래프를 아래와 같이 확인할 수 있습니다.
![image](https://github.com/user-attachments/assets/d6a64192-8a54-4f71-a469-b01a5f5dd488)
***
`streamlit run df.py`을 입력하시면 UN 농업 정보를 아래와 같이 확인할 수 있습니다.
![image](https://github.com/user-attachments/assets/dbebc4b1-ec35-489a-b1d2-e82610506be5)
- 국가를 추가하거나 제거할 수 있습니다.
***
### 사용된 라이브러리(dependency)
```python
import streamlit as st
import numpy as np
import pandas as pd
import altair as alt
from urllib.error import URLError
```
