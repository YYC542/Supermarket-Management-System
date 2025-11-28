FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY src/ ./src/
COPY tests/ ./tests/

CMD ["python", "-m", "pytest", "tests/", "-v"]
```
4. **Commit message**：
```
feat: add Dockerfile for containerization
```
5. **点击 "Commit new file"**

---

### 步骤3：创建 .dockerignore（可选但推荐）

1. **点击 "Add file" → "Create new file"**
2. **文件名**：`.dockerignore`
3. **内容**：
```
__pycache__/
*.pyc
*.pyo
*.pyd
.Python
*.so
*.egg
*.egg-info/
dist/
build/
.pytest_cache/
.coverage
htmlcov/
.git/
.github/
screenshots/
*.md
```
4. **Commit message**：
```
feat: add dockerignore to optimize image size
