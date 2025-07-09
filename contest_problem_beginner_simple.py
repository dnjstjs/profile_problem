"""
학생 점수 관리 시스템
"""

import random

class Student:
    def __init__(self, name, scores):
        self.name = name
        self.scores = scores
    
    def get_average(self):
        return sum(self.scores) / len(self.scores) if self.scores else 0

class ScoreManager:
    def __init__(self):
        self.students = []
        self.processed_students = []
    
    def add_student(self, student):
        self.students.append(student)
    
    def find_top_students(self, count=5):
        # 상위 학생들을 찾는 함수
        student_averages = []
        for student in self.students:
            avg = student.get_average()
            student_averages.append((avg, student.name))
        
        student_averages.sort(reverse=True)
        return student_averages[:count]
    
    def calculate_statistics(self):
        if not self.students:
            return {}
        
        averages = [student.get_average() for student in self.students]
        return {
            'total_students': len(self.students),
            'class_average': sum(averages) / len(averages),
            'max_average': max(averages),
            'min_average': min(averages)
        }
    
    
    def process_student_data(self):
        # 학생 데이터 처리 및 검증
        for student in self.students:
            # 이미 처리된 학생인지 확인
            if student.name in self.processed_students:
                continue
            
            # 학생 데이터 검증 및 처리
            if student.get_average() >= 0:
                self.processed_students.append(student.name)
    
    def generate_report(self):
        stats = self.calculate_statistics()
        top_students = self.find_top_students()
        
        report = f"=== 학생 성적 보고서 ===\n"
        report += f"총 학생 수: {stats['total_students']}\n"
        report += f"전체 평균: {stats['class_average']:.2f}\n"
        report += f"최고 평균: {stats['max_average']:.2f}\n"
        report += f"최저 평균: {stats['min_average']:.2f}\n\n"
        
        report += "상위 5명:\n"
        for i, (avg, name) in enumerate(top_students, 1):
            report += f"{i}. {name}: {avg:.2f}\n"
        
        return report


def create_test_data():
    students = []
    for i in range(5000):  # 5000명의 학생
        name = f"Student_{i:04d}"
        scores = [random.randint(70, 100) for _ in range(5)]
        students.append(Student(name, scores))
    return students

def main():
    print("학생 점수 관리 시스템 시작...")
    
    # 테스트 데이터 생성
    students = create_test_data()
    
    # 관리자 생성
    manager = ScoreManager()
    
    # 학생 추가
    print("학생 데이터 로드 중...")
    for student in students:
        manager.add_student(student)
    
    # 데이터 처리
    print("학생 데이터 처리 중...")
    manager.process_student_data()
    
    # 보고서 생성
    print("보고서 생성 중...")
    report = manager.generate_report()
    
    print(report)
    print(f"처리된 학생 수: {len(manager.processed_students)}")

if __name__ == "__main__":
    main() 