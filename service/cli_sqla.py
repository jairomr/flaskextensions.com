from dynaconf import settings
from github import Github
from sqlalchemy import Boolean, Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

github = Github(settings.GITHUB_TOKEN)

repositories = github.search_repositories(
    query=settings.SEARCH_QUERY, sort="stars"
)

engine = create_engine(settings.DATABASE_URL, echo=True)
session = sessionmaker(bind=engine)()
Base = declarative_base()


class Repo(Base):
    __tablename__ = "repos"

    id = Column(Integer, primary_key=True, autoincrement=False)
    name = Column(String)
    full_name = Column(String)
    archived = Column(Boolean)
    html_url = Column(String)

    def __repr__(self):
        return f"Repo {self.full_name}"


# command
Base.metadata.create_all(engine)


for item in repositories:
    repo = Repo(
        id=item.id,
        name=item.name,
        full_name=item.full_name,
        html_url=item.html_url,
    )
    session.add(repo)

session.commit()


print(session.query(Repo).filter_by(name="dynaconf").all())

# print(session.query(Repo).all())
