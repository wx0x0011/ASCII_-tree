def parse_txt_to_tree(lines):
    # 初始化一个栈用于跟踪当前节点层级，以及一个根节点列表
    stack = []
    root = []

    # 遍历每一行文本
    for i, line in enumerate(lines):
        if not line.strip():
            # 跳过空行
            continue
        # 计算当前行的缩进级别
        indent = len(line) - len(line.lstrip())
        # 创建一个节点，包含文本、缩进级别和子节点列表
        node = {"text": line.strip(), "indent": indent, "children": []}

        # 如果栈顶节点的缩进级别大于或等于当前节点，则弹出栈顶节点
        while stack and indent <= stack[-1]["indent"]:
            stack.pop()

        if stack:
            # 如果栈不为空，将当前节点添加为栈顶节点的子节点
            stack[-1]["children"].append(node)
        else:
            # 如果栈为空，将当前节点添加到根节点列表
            root.append(node)

        # 将当前节点压入栈
        stack.append(node)

    # 返回构建的树结构
    return root

def render_ascii_tree(nodes, prefix=""):
    # 初始化存储 ASCII 树的行列表
    lines = []
    # 获取当前节点列表的最后一个索引
    last_index = len(nodes) - 1
    for i, node in enumerate(nodes):
        # 根据是否是最后一个节点选择连接符
        connector = "└── " if i == last_index else "├── "
        # 添加当前节点的文本到行列表
        lines.append(prefix + connector + node["text"])
        # 为子节点生成新的前缀
        child_prefix = prefix + ("    " if i == last_index else "│   ")
        # 递归处理子节点，并将结果添加到行列表
        lines += render_ascii_tree(node["children"], child_prefix)
    # 返回生成的行列表
    return lines

def main():
    # 打开输入文件并读取所有行
    with open('structure.txt', 'r', encoding='utf-8') as f:
        lines = f.readlines()

    # 将文本解析为树结构
    tree = parse_txt_to_tree(lines)
    # 将树结构渲染为 ASCII 树
    ascii_lines = render_ascii_tree(tree)

    # 将 ASCII 树写入输出文件
    with open('ascii_tree.txt', 'w', encoding='utf-8') as f:
        f.write("\n".join(ascii_lines))

    # 打印生成成功的提示信息
    print("知识树 ASCII 图已生成：ascii_tree.txt")

# 如果脚本是直接运行的，则调用 main 函数
if __name__ == "__main__":
    main()