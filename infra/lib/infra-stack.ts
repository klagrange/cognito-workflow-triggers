import * as cdk from '@aws-cdk/core';
import * as apigateway from '@aws-cdk/aws-apigateway';

const apiLib = 'COGNITO-WORKFLOW-TRIGGERS';
const apiLibGatewayName = `${apiLib}-GATEWAY`

export class InfraStack extends cdk.Stack {
  constructor(scope: cdk.App, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    const api = new apigateway.RestApi(this, apiLibGatewayName, {
      deploy: false
    });
    api.root.addMethod('GET');


    new cdk.CfnOutput(this, 'restApiId', {
      value: api.restApiId,
      exportName: `${apiLib}-restApiId`,
    })
    new cdk.CfnOutput(this, 'restApiRootResourceId', {
      value: api.restApiRootResourceId,
      exportName: `${apiLib}-restApiRootResourceId`,
    })
  }
}
