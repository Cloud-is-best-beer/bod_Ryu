# Requirements
```bash
# python<=3.12
pip install -r requirements.txt
```

# How to Start
### 1. Set database

#### using sqlite
`config.py`
```python
SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(os.path.join(BASE_DIR, 'bod.db'))
```

#### using mysql
1. `download` mysql and base setting
2. `create` mysql user and database
   ```sql
    create database "bod";
    create user "you_id"@localhost identified by 'YOUR_PWD';
    grant all privilege on "bod".* to 'YOUR_ID'@'localhost';
   ```
3. `config.py`
   ```python
    # {0}=db user / {1}=db password
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{0}:{1}@localhost:3306/bod?charset=utf8'.format('YOUR_ID','YOUR_PWD')
   ```

### 2. Set key
```python
# session사용에 필요한 비밀키
SECRET_KEY = "my_key"
```

### 3. Set env
```bash
env_set.cmd
```

### 4. DB migrate
```bash
db_set.cmd
```

### 5. Run
```bash
flask run
```
