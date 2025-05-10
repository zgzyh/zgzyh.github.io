# random_ban.py - 动态生成随机禁点并通过GTP协议控制引擎
import subprocess
import random
import sys
import time

def generate_banned_points(width=15, num_points=5):
    """生成随机禁点坐标（例如：['A1', 'B2']）"""
    banned = set()
    while len(banned) < num_points:
        x = random.randint(0, width-1)
        y = random.randint(0, width-1)
        banned.add(f"{chr(x + 65)}{y+1}")  # 字母坐标（A-O） + 数字坐标（1-15）
    return list(banned)

def main():
    # 启动引擎进程（替换为你的引擎路径）
    engine_cmd = [
        "./engine/gom15x_trt.exe",
        "gtp",
        "-config", "./engine.cfg",
        "-model", "./weights/zhizi_renju28b_s1600.bin.gz",
        "-override-config", "basicRule=FREESTYLE"
    ]
    
    # 创建子进程并绑定输入输出管道
    engine = subprocess.Popen(
        engine_cmd,
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        bufsize=1,
        universal_newlines=True
    )
    
    # 生成5个随机禁点
    banned_points = generate_banned_points()
    for point in banned_points:
        engine.stdin.write(f"ban {point}\n")  # 发送GTP禁点命令
        print(f"[SCRIPT] 已设置禁点: {point}")
    
    engine.stdin.flush()
    
    # 持续监控引擎输出（可选）
    try:
        while True:
            line = engine.stdout.readline()
            if not line:
                break
            if "= " in line:  # GTP响应标识
                print(f"[ENGINE] {line.strip()}")
            time.sleep(0.1)
    except KeyboardInterrupt:
        print("\n[SCRIPT] 已终止脚本")
    finally:
        engine.terminate()

if __name__ == "__main__":
    main()