#!/usr/bin/env node
import * as cdk from '@aws-cdk/core';
import { InfraStack } from '../lib/infra-stack';

const app = new cdk.App();
new InfraStack(app, 'CognitoWorkflowTriggers', {
    env: {
        region: 'ap-southeast-1',
    }
});
