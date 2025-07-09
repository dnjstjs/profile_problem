# 초보자를 위한 프로파일링 문제 🔍

```bash
python3 -m venv venv
source venv/bin/activate && pip install line_profiler memory-profiler psutil
```


## 📋 문제 설명

이 문제는 **딱 한 줄**에만 숨겨진 성능 문제가 있는 초보자용 프로파일링 챌린지입니다.

**파일**: `contest_problem_beginner_simple.py`

코드를 보면 전반적으로 깔끔하고 문제없어 보이지만, 실제로 실행하면 성능이 예상보다 느립니다.

## 🎯 목표

1. **프로파일링 도구를 사용**하여 성능 병목점을 찾아라
2. **정확한 라인**을 특정하라
3. **해결책을 제시**하라

## 🔧 사용할 도구

### 1. cProfile (개괄적 분석)
```bash
python -m cProfile -s cumulative contest_problem_beginner_simple.py
```

### 2. line_profiler (라인별 분석)
```bash
kernprof -l -v contest_problem_beginner_simple.py
```

## 📊 예상 결과


## 🐛 문제 힌트

- 코드 리뷰만으로는 찾기 어려운 문제
- 자료구조와 관련된 문제
- O(n) vs O(n²) 복잡도 차이

## 💡 학습 포인트

1. **프로파일링의 중요성**: 코드 리뷰만으로는 찾기 어려운 성능 문제
2. **자료구조의 중요성**: 적절한 자료구조 선택이 성능에 미치는 영향
3. **도구 활용**: line_profiler로 정확한 문제 라인 특정

## 📁 파일 구조

```
contest_problem_beginner_simple.py          # 문제 파일
README_beginner_simple.md                   # 이 가이드
```

## 🏆 성공 기준

✅ 성능 병목점이 되는 정확한 라인 번호를 찾았는가?
✅ 왜 그 라인이 문제인지 설명할 수 있는가?
✅ 간단한 수정으로 성능을 대폭 개선했는가?

---

**💡 참고**: 이 문제는 실제 프로덕션 환경에서 자주 발생하는 실수를 기반으로 설계되었습니다. 프로파일링 도구 없이는 발견하기 어려운 **숨겨진 성능 킬러**입니다! 
