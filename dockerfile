# 使用基础的 conda 镜像
FROM continuumio/miniconda3

# 设置工作目录
WORKDIR /app

# 复制项目文件到工作目录
COPY . .

# 将 conda 虚拟环境复制到镜像中
COPY environment.yml /tmp/environment.yml
RUN conda env create -f /tmp/environment.yml && conda clean -af

# 设置环境变量
ENV PATH /opt/conda/envs/myenv/bin:$PATH
ENV CONDA_DEFAULT_ENV myenv

# 启动应用程序
CMD ["python", "1.py"]
