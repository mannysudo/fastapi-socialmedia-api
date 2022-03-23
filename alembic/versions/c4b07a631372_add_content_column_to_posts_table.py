"""Add content column to posts table

Revision ID: c4b07a631372
Revises: 49262cd9f6e7
Create Date: 2022-03-23 11:22:36.546525

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c4b07a631372'
down_revision = '49262cd9f6e7'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column('posts', 'content')
    pass
