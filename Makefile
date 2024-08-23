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