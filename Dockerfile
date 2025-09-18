FROM node:22-alpine

# Install bun
RUN curl -fsSL https://bun.sh/install | sh
ENV PATH="/root/.bun/bin:$PATH"

# Set working directory
WORKDIR /app

# Expose port 4000
EXPOSE 4000

# Default command
CMD ["sleep", "infinity"]
