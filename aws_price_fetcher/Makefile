######################
# Env Setup Commands #
######################

# Deploy

.PHONY: deploy
deploy:
	GASOLINE_API_URL="https://data.ny.gov/resource/wuxr-ni2i.json" serverless deploy --aws-profile developer_jhidalgo

# Kill lambda

.PHONY: kill
kill:
	serverless remove --aws-profile developer_jhidalgo

# Test locally
.PHONY: test_local
test_local:
	serverless invoke local -f price_fetcher --aws-profile developer_jhidalgo

# Invoke function
.PHONY: invoke
invoke:
	serverless invoke -f price_fetcher --log --aws-profile developer_jhidalgo