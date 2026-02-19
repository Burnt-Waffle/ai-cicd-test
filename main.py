from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "🚀 AI Pipeline is successfully running!"}

# [핵심] ASG와 Dev 배포 스크립트가 이 경로를 찔러서 배포 성공 여부를 판단합니다.
@app.get("/api/v1/health")
def health_check():
    return {"status": "healthy"}