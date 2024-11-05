<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>老夫叫老付呀</title>
    <style>
        /* 设置全屏动态背景动画 */
        body, html {
            margin: 0;
            padding: 0;
            width: 100%;
            height: 100%;
            overflow: hidden;
            display: flex;
            justify-content: center;
            align-items: center;
            background: linear-gradient(120deg, #ff9a9e, #fad0c4, #fad0c4, #ffecd2);
            background-size: 300% 300%;
            animation: backgroundAnimation 6s ease infinite;
            font-family: Arial, sans-serif;
            color: #fff;
        }

        @keyframes backgroundAnimation {
            0% { background-position: 0% 50%; }
            50% { background-position: 100% 50%; }
            100% { background-position: 0% 50%; }
        }

        /* 设置中心文本样式 */
        .center-text {
            font-size: 3rem;
            font-weight: bold;
            text-align: center;
            text-shadow: 2px 2px 8px rgba(0, 0, 0, 0.3);
        }
    </style>
</head>
<body>
    <div class="center-text">老夫叫老付呀</div>
</body>
</html>
