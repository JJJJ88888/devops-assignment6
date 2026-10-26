def add(a, b):
    # 解決衝突：保留 Bob 的安全型別轉換
    return int(a) + int(b)


def subtract(a, b):
    return a - b