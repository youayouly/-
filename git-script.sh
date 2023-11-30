#!/bin/bash

# 指定 JSON 文件路径
json_path="D:/storage/py/tasks.json"

# 从 JSON 文件中读取命令列表
commands=$(jq -c '.commands[]' "$json_path")

# 逐条执行命令
while IFS= read -r command; do
    # 直接从 JSON 中提取 command 属性
    cmd=$(jq -r '.command' <<< "$command")
    description=$(jq -r '.description' <<< "$command")

    echo "Executing: $description"
    
    # 添加调试信息
    echo "Command to be executed: $cmd"
    
    eval "$cmd"
    
    # 添加调试信息
    echo "Command executed: $cmd"
done <<< "$commands"

echo "Script executed successfully"
