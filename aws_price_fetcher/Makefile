# Makefile: common make commands used for local development

######################
# Env Setup Commands #
######################

# Deploy

.PHONY: deploy
deploy:
	serverless deploy

# Kill lambda

.PHONY: kill
kill:
	serverless remove

# Test locally
.PHONY: test_local
test_local:
	serverless invoke -f compute --log