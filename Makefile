build:
	@echo "Building..."
	@cd src/backend && poetry install
	@cd src/frontend && fnm use v18.17 && pnpm install && pnpm run build
backend:
	@echo "Start backend..."
	@cd src/backend && poetry run python main.py
frontend:
	@echo "Start frontend..."
	@cd src/frontend && fnm use v18.17 && pnpm dev
gernate:
	@echo "Generate..."
	@cd src/backend && poetry run generate
data:
	@echo "Data..."
	@cd src/backend/crawler && poetry run python crawl.py