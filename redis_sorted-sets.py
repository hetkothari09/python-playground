import redis

r = redis.Redis(
    host='localhost',
    port=6379,
    db=0
)

def add_tags(post_id, tag):
    r.sadd(f"post:{post_id}:tags", tag)
    print("Tag added....")
def get_tags(post_id):
    data = r.smembers(f"post:{post_id}:tags")
    print({x.decode() for x in data})

def update_leaderboard(name, score):
    r.zadd(f"game:leaderboard", {name:score})
    print("Leaderboard updated....")

def get_leaderboard(name):
    data = r.zrange("game:leaderboard", 0, -1, withscores=True)
    print({x.decode(): y for x, y in data})

if __name__ == '__main__':
    add_tags(100, "python")
    add_tags(100, "react")
    add_tags(100, "fastapi")
    add_tags(101, "react")

    get_tags(100)
    get_tags(101)

    update_leaderboard("Het", 400)
    update_leaderboard("John", 100)
    update_leaderboard("Doe", 200)

    get_leaderboard("Het")