# Push-to-deploy without a key (run these once)

The deploy workflow now authenticates with Workload Identity Federation: GitHub's OIDC token is exchanged for a dedicated deploy service account. No JSON key is created or stored. These steps grant permissions, so they must be run by the project owner.

```bash
SA=aiapply-cursor-agent@aiapply-ch.iam.gserviceaccount.com; P=aiapply-ch; REPO=adamripon-ship-it/juzlova-rebuild-status
G="gcloud --account $SA --project $P --quiet"
$G services enable iamcredentials.googleapis.com sts.googleapis.com cloudbuild.googleapis.com artifactregistry.googleapis.com run.googleapis.com
$G iam workload-identity-pools create github --location=global --display-name="GitHub Actions"
$G iam workload-identity-pools providers create-oidc github-oidc --location=global --workload-identity-pool=github \
  --display-name="GitHub OIDC" --issuer-uri="https://token.actions.githubusercontent.com" \
  --attribute-mapping="google.subject=assertion.sub,attribute.repository=assertion.repository,attribute.ref=assertion.ref" \
  --attribute-condition="assertion.repository == '$REPO'"
$G iam service-accounts create github-deploy --display-name="GitHub Actions deploy (juzlova-web)"
DSA=github-deploy@$P.iam.gserviceaccount.com
for r in roles/run.admin roles/cloudbuild.builds.editor roles/storage.admin roles/artifactregistry.writer roles/iam.serviceAccountUser roles/serviceusage.serviceUsageConsumer roles/viewer; do
  $G projects add-iam-policy-binding $P --member="serviceAccount:$DSA" --role=$r --condition=None; done
PN=$($G projects describe $P --format='value(projectNumber)')
$G iam service-accounts add-iam-policy-binding $DSA --role=roles/iam.workloadIdentityUser \
  --member="principalSet://iam.googleapis.com/projects/$PN/locations/global/workloadIdentityPools/github/attribute.repository/$REPO"
gh variable set GCP_PROJECT --body "$P"
gh variable set GCP_WIF_PROVIDER --body "projects/$PN/locations/global/workloadIdentityPools/github/providers/github-oidc"
gh variable set GCP_DEPLOY_SA --body "$DSA"
```

Then push any commit (or run the workflow manually) and check the "Deploy" step prints a new revision.
